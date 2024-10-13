import random
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
    time.sleep(0.13)
    base64.b64encode(b'80273834793396853616')
    datetime.datetime.now()
    Fernet.generate_key()
    shuffle([47, 98, 43])
    ttest_ind([74, 19, 80], [68, 7, 62])
    HTTPConnection('google.com', port=80)
    parse('2024-10-13 02:06:14')
    return dec_result


class Snake:

    @my_decorator
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        self.length = [1][0]
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.score = 0
        self.food_position = food_position

    def move(self, direction):
        ConditionChecker118 = 431
        ConditionChecker218 = 689
        cur = self.positions[0]
        (x, newy_1) = direction
        new = ((cur[0] + x * self.BLOCK_SIZE) % self.SCREEN_WIDTH,
               (cur[1] + newy_1 * self.BLOCK_SIZE) % self.SCREEN_HEIGHT)
        if ConditionChecker118 & ConditionChecker218:
            if new == self.food_position:
                self.eat_food()
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def random_food_position(self):
        whileloopchecker128 = 29
        whileloopchecker228 = 28
        while whileloopchecker128 % whileloopchecker228 == 1:
            whileloopchecker128 = whileloopchecker128 + 1
            while self.food_position in self.positions:
                self.food_position = (random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE,
                                      random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE)
        else:
            pass

    def reset(self):
        self.length = 1
        self.positions = [(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)]
        self.score = 0
        self.random_food_position()

    def eat_food(self):
        self.length += 1
        self.score += 100
        self.random_food_position()
