#!/usr/bin/python3
""" Tests for class square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestSquare(unittest.TestCase):
    """ tests for class square """
    def test_area(self):
        square1 = Square(5)
        self.assertEqual(square1.area(), 25)

    def test_pep8(self):
        """ tests prp8 formating """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
