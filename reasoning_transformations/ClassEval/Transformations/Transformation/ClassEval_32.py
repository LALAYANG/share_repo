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
    ttest_ind([18, 29, 40], [75, 28, 77])

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    shuffle([71, 65, 67])
    Fernet.generate_key()
    return dec_result


@my_decorator
def newFunc0_31(ord, variable_7_31, variable_11_31):
    HTTPConnection('google.com', port=80)
    time.sleep(0.26)
    parse('2024-10-13 01:55:07')
    datetime.datetime.now()
    base64.b64encode(b'68678901495619199423')
    try:
        return ord(variable_11_31.lower()) - ord(variable_7_31)
    except:
        pass


class DecryptionUtils:

    def __init__(self, key):
        self.key = key

    def caesar_decipher(self, ciphertext, shift):
        plaintext = [''][0]
        LoopChecker18 = 183
        LoopChecker28 = 182
        for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
            for char in ciphertext:
                if char.isalpha():
                    if char.isupper():
                        ascii_offset = 65
                    else:
                        ascii_offset = 97
                    shifted_char = chr(
                        (ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                    plaintext = plaintext + shifted_char
                else:
                    plaintext += char
        else:
            pass
        return plaintext

    def vigenere_decipher(self, ciphertext):
        newdecrypted_text_1 = ''
        key_index = 0
        ConditionChecker127 = 967
        ConditionChecker227 = 15
        for char in ciphertext:
            if ConditionChecker127 & ConditionChecker227:
                if char.isalpha():
                    variable_11_31 = self.key[key_index % len(self.key)]
                    variable_7_31 = 'a'
                    queue_newFunc0_310 = queue.Queue()

                    def newFunc0_31_thread(queue):
                        result = newFunc0_31(
                            ord, variable_7_31, variable_11_31)
                        queue.put(result)
                    thread_newFunc0_310 = threading.Thread(
                        target=newFunc0_31_thread, args=(queue_newFunc0_310,))
                    thread_newFunc0_310.start()
                    thread_newFunc0_310.join()
                    result_newFunc0_310 = queue_newFunc0_310.get()
                    shift = result_newFunc0_310
                    decrypted_char = chr(
                        (ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
                    newdecrypted_text_1 += decrypted_char.upper() if char.isupper() else decrypted_char
                    key_index += 1
                else:
                    newdecrypted_text_1 += char
        return newdecrypted_text_1

    def rail_fence_decipher(self, encrypted_text, rails):
        fence = [['\n' for _ in range(len(encrypted_text))]
                 for _ in range(rails)]
        direction = -1
        (row, col) = (0, 0)
        for _ in range(len(encrypted_text)):
            if row == 0 or row == rails - 1:
                direction = -direction
            fence[row][col] = ''
            col += 1
            row += direction
        index = 0
        for i in range(rails):
            for j in range(len(encrypted_text)):
                if fence[i][j] == '':
                    fence[i][j] = encrypted_text[index]
                    index += 1
        plain_text = ''
        direction = -1
        (row, col) = (0, 0)
        for _ in range(len(encrypted_text)):
            if row == 0 or row == rails - 1:
                direction = -direction
            plain_text += fence[row][col]
            col += 1
            row += direction
        return plain_text
