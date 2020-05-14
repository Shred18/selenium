
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('https://www.mercari.com/')
        print('Mercari Opened')