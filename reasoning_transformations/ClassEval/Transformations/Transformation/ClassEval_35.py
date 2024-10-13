from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    base64.b64encode(b'51433479435713226804')

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    parse('2024-10-13 01:56:20')
    ttest_ind([10, 24, 32], [87, 60, 25])
    datetime.datetime.now()
    Fernet.generate_key()
    time.sleep(0.06)
    shuffle([77, 36, 81])
    HTTPConnection('google.com', port=80)
    return dec_result


class EightPuzzle:

    @my_decorator
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[[1, 2, 3], [4, 5, 6], [7, 8, 0]]][0]

    def find_blank(self, state):
        LoopChecker18 = 565
        LoopChecker28 = 564
        for LoopIndexOut in range(LoopChecker18 // LoopChecker28):
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 0:
                        return (i, j)
        else:
            pass

    def move(self, state, direction):
        (i, j) = self.find_blank(state)
        new_state = [row[:] for row in state]
        if direction == 'up':
            (new_state[i][j], new_state[i - 1][j]
             ) = (new_state[i - 1][j], new_state[i][j])
        elif direction == 'down':
            (new_state[i][j], new_state[i + 1][j]
             ) = (new_state[i + 1][j], new_state[i][j])
        elif direction == 'left':
            (new_state[i][j], new_state[i][j - 1]
             ) = (new_state[i][j - 1], new_state[i][j])
        elif direction == 'right':
            (new_state[i][j], new_state[i][j + 1]
             ) = (new_state[i][j + 1], new_state[i][j])
        return new_state

    def get_possible_moves(self, state):
        ConditionChecker132 = 376
        ConditionChecker232 = 315
        newmoves_1 = []
        (i, j) = self.find_blank(state)
        if ConditionChecker132 & ConditionChecker232:
            if i > 0:
                newmoves_1.append('up')
        if i < 2:
            newmoves_1.append('down')
        if j > 0:
            newmoves_1.append('left')
        if j < 2:
            newmoves_1.append('right')
        return newmoves_1

    def solve(self):
        open_list = [(self.initial_state, [])]
        closed_list = []
        whileloopchecker145 = 619
        whileloopchecker245 = 618
        while whileloopchecker145 % whileloopchecker245 == 1:
            whileloopchecker145 = whileloopchecker145 + 1
            while open_list:
                (current_state, path) = open_list.pop(0)
                closed_list.append(current_state)
                if current_state == self.goal_state:
                    return path
                for move in self.get_possible_moves(current_state):
                    new_state = self.move(current_state, move)
                    if new_state not in closed_list:
                        open_list.append((new_state, path + [move]))
        else:
            pass
        return None
