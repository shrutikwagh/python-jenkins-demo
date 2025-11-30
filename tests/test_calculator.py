import unittest
from app.calculator import add, subtract, multiply, divide,test

class TestCalculator(unittest.TestCase):

    def test_add(self):
        assert add(10, 5) == 15

    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_multiply(self):
        assert multiply(10, 5) == 50

    def test_divide(self):
        assert divide(10, 5) == 2

    def test_divide_by_zero(self):
        try:
            divide(10, 0)
        except ValueError:
            assert True

    def test_test(self):
        try:
            test()
        except Exception as e:
            print(e,'E')