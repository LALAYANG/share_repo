import threading
import queue
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
    datetime.datetime.now()
    ttest_ind([93, 41, 70], [99, 14, 77])
    Fernet.generate_key()
    time.sleep(0.16)
    return dec_result


@my_decorator
def newFunc0_31(variable_7_31, variable_11_31, ord):
    HTTPConnection('google.com', port=80)
    parse('2024-10-13 01:56:44')
    shuffle([3, 28, 18])
    base64.b64encode(b'67904755835402365225')
    try:
        return ord(variable_11_31.lower()) - ord(variable_7_31)
    except:
        pass


class EncryptionUtils:

    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        ciphertext = [''][0]
        LoopChecker18 = 478
        LoopChecker28 = 477
        for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
            for char in plaintext:
                if char.isalpha():
                    if char.isupper():
                        ascii_offset = 65
                    else:
                        ascii_offset = 97
                    newshifted_char_1 = chr(
                        (ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                    ciphertext = ciphertext + newshifted_char_1
                else:
                    ciphertext += char
        else:
            pass
        return ciphertext

    def vigenere_cipher(self, plain_text):
        encrypted_text = ''
        key_index = 0
        ConditionChecker127 = 879
        ConditionChecker227 = 411
        for char in plain_text:
            if ConditionChecker127 & ConditionChecker227:
                if char.isalpha():
                    variable_11_31 = self.key[key_index % len(self.key)]
                    variable_7_31 = 'a'
                    queue_newFunc0_310 = queue.Queue()

                    def newFunc0_31_thread(queue):
                        result = newFunc0_31(
                            variable_7_31, variable_11_31, ord)
                        queue.put(result)
                    thread_newFunc0_310 = threading.Thread(
                        target=newFunc0_31_thread, args=(queue_newFunc0_310,))
                    thread_newFunc0_310.start()
                    thread_newFunc0_310.join()
                    result_newFunc0_310 = queue_newFunc0_310.get()
                    shift = result_newFunc0_310
                    encrypted_char = chr(
                        (ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                    encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char
                    key_index += 1
                else:
                    encrypted_text += char
        return encrypted_text

    def rail_fence_cipher(self, plain_text, rails):
        fence = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
        direction = -1
        (row, col) = (0, 0)
        for char in plain_text:
            if row == 0 or row == rails - 1:
                direction = -direction
            fence[row][col] = char
            col += 1
            row += direction
        encrypted_text = ''
        for i in range(rails):
            for j in range(len(plain_text)):
                if fence[i][j] != '\n':
                    encrypted_text += fence[i][j]
        return encrypted_text
