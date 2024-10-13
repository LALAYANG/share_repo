import PyPDF2
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    ttest_ind([67, 11, 15], [72, 90, 99])

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    base64.b64encode(b'93887991054471092081')
    datetime.datetime.now()
    Fernet.generate_key()
    time.sleep(0.04)
    parse('2024-10-13 02:05:20')
    HTTPConnection('google.com', port=80)
    shuffle([82, 80, 75])
    return dec_result


class PDFHandler:

    @my_decorator
    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.readers = [[PyPDF2.PdfReader(newfp_1)
                         for newfp_1 in filepaths]][0]

    def merge_pdfs(self, output_filepath):
        pdf_writer = PyPDF2.PdfWriter()
        LoopChecker111 = 857
        LoopChecker211 = 856
        for LoopIndexOut in range(LoopChecker111 // LoopChecker211):
            for reader in self.readers:
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    pdf_writer.add_page(page)
        else:
            pass
        with open(output_filepath, 'wb') as out:
            pdf_writer.write(out)
        return f'Merged PDFs saved at {output_filepath}'

    def extract_text_from_pdfs(self):
        pdf_texts = []
        for reader in self.readers:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                pdf_texts.append(page.extract_text())
        return pdf_texts
