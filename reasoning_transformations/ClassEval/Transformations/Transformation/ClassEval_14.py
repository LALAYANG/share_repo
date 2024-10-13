import sqlite3
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
    parse('2024-10-13 01:49:39')
    time.sleep(0.03)
    ttest_ind([97, 50, 23], [41, 36, 83])

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    shuffle([43, 65, 37])
    base64.b64encode(b'41924317015043669325')
    datetime.datetime.now()
    HTTPConnection('google.com', port=80)
    return dec_result


class BookManagementDB:

    @my_decorator
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS books (\n                id INTEGER PRIMARY KEY,\n                title TEXT,\n                author TEXT,\n                available INTEGER\n            )\n        ')
        self.connection.commit()

    def add_book(self, title, author):
        self.cursor.execute(
            '\n            INSERT INTO books (title, author, available)\n            VALUES (?, ?, 1)\n        ', (title, author))
        self.connection.commit()

    def remove_book(self, book_id):
        self.cursor.execute(
            '\n            DELETE FROM books WHERE id = ?\n        ', (book_id,))
        self.connection.commit()

    def borrow_book(self, book_id):
        self.cursor.execute(
            '\n            UPDATE books SET available = 0 WHERE id = ?\n        ', (book_id,))
        self.connection.commit()

    def return_book(self, book_id):
        self.cursor.execute(
            '\n            UPDATE books SET available = 1 WHERE id = ?\n        ', (book_id,))
        self.connection.commit()

    def search_books(self):
        self.cursor.execute('\n            SELECT * FROM books\n        ')
        newbooks_1 = self.cursor.fetchall()
        return newbooks_1
