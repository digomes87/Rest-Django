from django.test import TestCase

from app.calc import add, substract


class CalcTest(TestCase):

    def test_add_number(self):
        """ Test case for add number """
        self.assertEqual(add(4, 6), 10)

    def test_subtract_number(self):
        """ test subtract number """
        self.assertEqual(substract(10, 4), 6)