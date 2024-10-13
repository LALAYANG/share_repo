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
    base64.b64encode(b'90959103613150934760')
    HTTPConnection('google.com', port=80)
    shuffle([1, 35, 19])
    parse('2024-10-13 02:04:08')
    time.sleep(0.06)
    ttest_ind([70, 22, 11], [66, 91, 84])
    datetime.datetime.now()

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    Fernet.generate_key()
    return dec_result


class MovieTicketDB:

    @my_decorator
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS tickets (\n                id INTEGER PRIMARY KEY,\n                movie_name TEXT,\n                theater_name TEXT,\n                seat_number TEXT,\n                customer_name TEXT\n            )\n        ')
        self.connection.commit()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        self.cursor.execute('\n            INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)\n            VALUES (?, ?, ?, ?)\n        ',
                            (movie_name, theater_name, seat_number, customer_name))
        self.connection.commit()

    def search_tickets_by_customer(self, customer_name):
        self.cursor.execute(
            '\n            SELECT * FROM tickets WHERE customer_name = ?\n        ', (customer_name,))
        newtickets_1 = self.cursor.fetchall()
        return newtickets_1

    def delete_ticket(self, ticket_id):
        self.cursor.execute(
            '\n            DELETE FROM tickets WHERE id = ?\n        ', (ticket_id,))
        self.connection.commit()
