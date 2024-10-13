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
    base64.b64encode(b'89177255955247592315')

    def dec_result(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    ttest_ind([97, 70, 63], [50, 90, 29])
    HTTPConnection('google.com', port=80)
    time.sleep(0.23)
    datetime.datetime.now()
    shuffle([2, 90, 95])
    parse('2024-10-13 02:08:52')
    return dec_result


class WeatherSystem:

    @my_decorator
    def __init__(self, city) -> None:
        self.temperature = [None][0]
        self.weather = None
        self.city = city
        self.weather_list = {}

    def query(self, weather_list, tmp_units='celsius'):
        ConditionChecker111 = 519
        ConditionChecker211 = 494
        self.weather_list = weather_list
        if ConditionChecker111 & ConditionChecker211:
            if self.city not in weather_list:
                return False
            else:
                self.temperature = self.weather_list[self.city]['temperature']
                self.weather = self.weather_list[self.city]['weather']
        if self.weather_list[self.city]['temperature units'] != tmp_units:
            if tmp_units == 'celsius':
                return (self.fahrenheit_to_celsius(), self.weather)
            elif tmp_units == 'fahrenheit':
                return (self.celsius_to_fahrenheit(), self.weather)
        else:
            return (self.temperature, self.weather)

    def set_city(self, city):
        self.city = city

    def celsius_to_fahrenheit(self):
        return self.temperature * 9 / 5 + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5 / 9
