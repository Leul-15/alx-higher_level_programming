#!/usr/bin/python3
""" Tests for class Base """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestBase(unittest.TestCase):
    """ tests for class base """

    def test_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)
        base4 = Base(12)
        self.assertEqual(base4.id, 12)
        base5 = Base()
        self.assertEqual(base5.id, 4)
        with self.assertRaises(TypeError):
            Base(5, 6)

    def test_pep8(self):
        """ tests prp8 formating """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
