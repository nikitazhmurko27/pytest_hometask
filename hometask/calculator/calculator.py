""" Home task calculator module """
from math import sqrt


class Calculator:
    """ Calculator implementation """

    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        self.is_int(x, y)
        return x + y

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        self.is_int(x, y)
        return x - y

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        self.is_int(x, y)
        if y <= 0:
            raise ValueError()
        return x / y

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        self.is_int(x, y)
        return x * y

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        self.is_int(x, y)
        return x % y

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        self.is_int(x, y)
        return x ** y

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        self.is_int(x, 1)
        if x <= 0:
            raise ValueError()
        return sqrt(x)

    def is_int(self, x, y):
        """Checks if the numbers are int"""
        if not isinstance(x, int):
            raise TypeError()
        if not isinstance(y, int):
            raise TypeError()
