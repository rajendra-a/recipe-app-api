"""
Sample tests
"""
import imp
from re import I
from django.test import SimpleTestCase

from app import calc         

class CalcTests(SimpleTestCase):
    """Test calc module """
    def test_add_numbers(self):
        res = calc.add(2,4)   

        self.assertEqual(res, 6)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)