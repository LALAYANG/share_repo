import coverage
import subprocess
import os
import sys
import pygraphviz as pgv
import networkx as nx
from py2cfgPlus.py2cfgPlus.builder import CFGBuilder

def extract_all_simple_paths(graph):
    nodes = list(graph.nodes)
    all_paths = []
    for start_node in nodes:
        for end_node in nodes:
            if start_node != end_node:
                paths = list(nx.all_simple_paths(graph, start_node, end_node))
                all_paths.extend(paths)
    return all_paths

def is_prime_path(path, all_paths):
    # longest simple path that is not sub of others
    for other_path in all_paths:
        if path != other_path and len(path) <= len(other_path):
            if any(path == other_path[i:i+len(path)] for i in range(len(other_path) - len(path) + 1)):
                return False
    return True

def generate_prime_paths(cfg):
    all_paths = extract_all_simple_paths(cfg)
    prime_paths = [path for path in all_paths if is_prime_path(path, all_paths)]
    return prime_paths

def get_prime_paths(python_file):
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_file('CFG', python_file)
    cfg.build_visual(f'CFG_{python_file}', 'dot')
    cfg.build_visual(f'CFG_{python_file}', 'png')
    G = pgv.AGraph(f"CFG_{python_file}.dot")
    nx_graph = nx.nx_agraph.from_agraph(G)
    # for node in nx_graph.nodes:
    #     print(nx_graph.nodes[node]['label'])
    #     print(nx_graph.nodes[node]['linenum'])
    #     exit(0)
    
    prime_paths = generate_prime_paths(nx_graph)
    prime_paths_stats = []
    for path in prime_paths:
        stats = [nx_graph.nodes[node].get('label') for node in path]
        prime_paths_stats.append(stats)
        print("Prime Path:", stats)
    return prime_paths, prime_paths_stats, nx_graph


def run_coverage(script):
    try:
        subprocess.run(['coverage', 'run', script], check=True)
        result = subprocess.run(['coverage', 'report', '-m'], check=True, capture_output=True, text=True)
        write_file(script + "_cov.txt", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running coverage: {e.stderr}")
    
    cov = coverage.Coverage()
    cov.load()
    covered_statements_linenos = []
    missing_statements_linenos = []
    for filename in cov.get_data().measured_files():
        executed_lines = cov.get_data().lines(filename)
        for line in executed_lines:
            covered_statements_linenos.append(line)
        missing_statements_linenos = cov.analysis(filename)[2]
        print(f"Covered statements in {filename}: {sorted(executed_lines)} Missing statements: {sorted(missing_statements_linenos)}")
    
    subprocess.run(['coverage', 'erase'], check=True)

    return covered_statements_linenos, missing_statements_linenos


def read_file(file_path):
    file = open(file_path, 'r')
    content = file.read()
    return content

def write_file(file_path,content):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    except:
        pass
    f = open(file_path, "w")
    f.write(content)
    f.close()
    
def get_prime_path_coverage(prime_paths, missing_statements_linenos, combination_file, nx_graph):
    # missing_statements = [get_statement_from_line(combination_file, lineno) for lineno in missing_statements_linenos]
    covered_paths = []
    for prime_path in prime_paths:
        prime_path_linenos = [int(nx_graph.nodes[node]['linenum']) for node in prime_path]
        path_missed = bool(set(prime_path_linenos) & set(missing_statements_linenos))
        # print(prime_path_linenos, missing_statements_linenos, path_missed)
        if not path_missed:
            covered_paths.append(prime_path)
        else:
            print("Missing paths (linenums):", prime_path_linenos)
            
    print("#Covered prime paths:", len(covered_paths), "\n#Total prime paths:",len(prime_paths))
    
    return covered_paths

def get_statement_from_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if 1 <= line_number <= len(lines):
            return lines[line_number - 1].strip()
        else:
            return f"Error: Line number {line_number} is out of range. The file has {len(lines)} lines."

    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    args = sys.argv[1:]
    python_file = args[0]
    input_file = args[1]
    combination_file = f"test_{python_file}"
    write_file(combination_file, f"{read_file(python_file)}\n{read_file(input_file)}")
    prime_paths, prime_paths_stats, nx_graph = get_prime_paths(combination_file)
    covered_statements_linenos, missing_statements_linenos = run_coverage(combination_file)
    get_prime_path_coverage(prime_paths, missing_statements_linenos, combination_file, nx_graph)