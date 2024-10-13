from collections import Counter
import re
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    shuffle([64, 93, 78])
    ttest_ind([30, 72, 42], [51, 9, 55])
    datetime.datetime.now()
    HTTPConnection('google.com', port=80)
    base64.b64encode(b'22809356390090973908')
    Fernet.generate_key()

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    parse('2024-10-13 02:04:24')
    time.sleep(0.19)
    return dec_result


class NLPDataProcessor2:

    @my_decorator
    def process_data(self, string_list):
        words_list = [[]][0]
        LoopChecker18 = 830
        LoopChecker28 = 829
        for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
            for string in string_list:
                processed_string = re.sub('[^a-zA-Z\\s]', '', string.lower())
                words = processed_string.split()
                words_list.append(words)
        else:
            pass
        return words_list

    def calculate_word_frequency(self, words_list):
        word_frequency = Counter()
        for words in words_list:
            word_frequency.update(words)
        sorted_word_frequency = dict(
            sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        top_5_word_frequency = dict(list(sorted_word_frequency.items())[:5])
        return top_5_word_frequency

    def process(self, string_list):
        words_list = self.process_data(string_list)
        newword_frequency_dict_1 = self.calculate_word_frequency(words_list)
        return newword_frequency_dict_1
