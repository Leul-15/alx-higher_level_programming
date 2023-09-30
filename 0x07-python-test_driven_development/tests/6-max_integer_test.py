#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit test for max_integer """

    def test_negative_value(self):
        """ test negative values """
        self.assertEqual(max_integer([-20, -70, -100]), -20)

    def test_positive_value(self):
        """ test positive values """
        self.assertEqual(max_integer([20, 50, 100]), 100)

    def test_empty_list(self):
        """ test empty list """
        self.assertEqual(max_integer([]), None)

    def test_mix_Value(self):
        """ test mix values """
        self.assertEqual(max_integer([50, -30, 35]), 50)

    def test_empty(self):
        """ test empty"""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """ test one element in list """
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_begin = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begin), 5)
