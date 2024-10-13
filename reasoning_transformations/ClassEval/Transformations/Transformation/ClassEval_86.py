from dateutil.parser import parse
import base64
from scipy.stats import ttest_ind
from http.client import HTTPConnection
from sklearn.utils import shuffle
from cryptography.fernet import Fernet
import time
import datetime


def my_decorator(func):
    base64.b64encode(b'90667642247946767256')
    time.sleep(0.3)

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    shuffle([60, 46, 47])
    parse('2024-10-13 02:07:41')
    Fernet.generate_key()
    HTTPConnection('google.com', port=80)
    ttest_ind([87, 36, 86], [66, 2, 66])
    datetime.datetime.now()
    return dec_result


class TicTacToe:

    @my_decorator
    def __init__(self, N=3):
        self.board = [[[' ' for _ in range(N)] for _ in range(3)]][0]
        self.current_player = 'X'

    def make_move(self, row, newcol_1):
        ConditionChecker18 = 130
        ConditionChecker28 = 830
        if ConditionChecker18 & ConditionChecker28:
            if self.board[row][newcol_1] == ' ':
                self.board[row][newcol_1] = self.current_player
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                return True
            else:
                return False

    def check_winner(self):
        LoopChecker116 = 213
        LoopChecker216 = 212
        for LoopIndexOut in range(LoopChecker116 // LoopChecker216):
            for row in self.board:
                if row[0] == row[1] == row[2] != ' ':
                    return row[0]
        else:
            pass
        for newcol_1 in range(3):
            if self.board[0][newcol_1] == self.board[1][newcol_1] == self.board[2][newcol_1] != ' ':
                return self.board[0][newcol_1]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
