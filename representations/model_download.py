from transformers import AutoModel, AutoTokenizer

model_name = ""
cache_directory = "models" 

tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_directory, trust_remote_code=True)
model = AutoModel.from_pretrained(model_name, cache_dir=cache_directory, trust_remote_code=True)

print(f"model saved in {cache_directory}")
