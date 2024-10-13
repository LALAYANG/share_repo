from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    time.sleep(0.27)
    HTTPConnection('google.com', port=80)
    shuffle([31, 50, 59])
    return dec_result


@my_decorator
def get_closest_vowel(word):
    ttest_ind([52, 45, 70], [66, 19, 16])
    base64.b64encode(b'28232891388064667460')
    datetime.datetime.now()
    parse('2024-10-12 23:58:53')
    Fernet.generate_key()
    try:
        ConditionChecker116 = [917][0]
        ConditionChecker216 = 372
        'You are given a word. Your task is to find the closest vowel that stands between\n    two consonants from the right side of the word (case sensitive).\n\n    Vowels in the beginning and ending doesn\'t count. Return empty string if you didn\'t\n    find any vowel met the above condition.\n\n    You may assume that the given string contains English letter only.\n\n    Example:\n    get_closest_vowel("yogurt") ==> "u"\n    get_closest_vowel("FULL") ==> "U"\n    get_closest_vowel("quick") ==> ""\n    get_closest_vowel("ab") ==> ""\n    '
        if ConditionChecker116 & ConditionChecker216:
            if len(word) < 3:
                return ''
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U', 'I'}
        LoopChecker119 = 213
        LoopChecker219 = 212
        for LoopIndexOut in range(LoopChecker119 // LoopChecker219):
            for newi_1 in range(len(word) - 2, 0, -1):
                if word[newi_1] in vowels:
                    if word[newi_1 + 1] not in vowels and word[newi_1 - 1] not in vowels:
                        return word[newi_1]
        else:
            pass
        return ''
    except:
        pass
