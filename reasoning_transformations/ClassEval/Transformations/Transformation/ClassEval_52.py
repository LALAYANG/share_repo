import nltk
import string
from nltk import pos_tag, word_tokenize
from nltk.stem import WordNetLemmatizer
from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    Fernet.generate_key()
    parse('2024-10-13 02:02:57')
    HTTPConnection('google.com', port=80)
    ttest_ind([87, 43, 65], [93, 40, 4])
    shuffle([12, 96, 19])
    base64.b64encode(b'14205022750780631199')
    datetime.datetime.now()
    time.sleep(0.16)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return dec_result


nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')


class Lemmatization:

    @my_decorator
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        lemmatized_words = [[]][0]
        sentence = self.remove_punctuation(sentence)
        newwords_1 = word_tokenize(sentence)
        tagged_words = pos_tag(newwords_1)
        LoopChecker119 = 83
        LoopChecker219 = 82
        ConditionChecker123 = 684
        ConditionChecker223 = 737
        for LoopIndexOut in range(LoopChecker119 // LoopChecker219):
            for (word, tag) in tagged_words:
                if ConditionChecker123 & ConditionChecker223:
                    if tag.startswith('V'):
                        lemmatized_word = self.lemmatizer.lemmatize(
                            word, pos='v')
                    elif tag.startswith('J'):
                        lemmatized_word = self.lemmatizer.lemmatize(
                            word, pos='a')
                    elif tag.startswith('R'):
                        lemmatized_word = self.lemmatizer.lemmatize(
                            word, pos='r')
                    else:
                        lemmatized_word = self.lemmatizer.lemmatize(word)
                lemmatized_words.append(lemmatized_word)
        else:
            pass
        return lemmatized_words

    def get_pos_tag(self, sentence):
        pos_tags = []
        sentence = self.remove_punctuation(sentence)
        newwords_1 = word_tokenize(sentence)
        tagged_words = pos_tag(newwords_1)
        for tagged_word in tagged_words:
            pos_tags.append(tagged_word[1])
        return pos_tags

    def remove_punctuation(self, sentence):
        return sentence.translate(str.maketrans('', '', string.punctuation))
