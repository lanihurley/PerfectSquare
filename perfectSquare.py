"""
Author: Lani Hurley
Date: 5/16/2022
Filename: perfectSquare.py is a Python program that will print a boolean value (True or False) to check if an integer
number is a perfect square.

*Must import math from Python
"""
import math


def is_square(n):

    print(bool(n > -1 and math.sqrt(n) % 1 == 0))


is_square(n=3)
