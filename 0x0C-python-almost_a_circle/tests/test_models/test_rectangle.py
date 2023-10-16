#!/usr/bin/python3

"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_order_of_initialization
    TestRectangle_area
    TestRectangle_update_args
    TestRectangle_update_kwargs
    TestRectangle_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        rectangle = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rectangle.area())

    def test_area_changed_attributes(self):
        rectangle = Rectangle(2, 10, 1, 1, 1)
        rectangle.width = 7
        rectangle.height = 14
        self.assertEqual(98, rectangle.area())

    def test_area_one_arg(self):
        rectangle = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rectangle.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    def test_str_method_print_width_height(self):
        rectangle = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(rectangle, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(rectangle.id)
        self.assertEqual(correct, capture.getvalue())


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rectangle))

    def test_update_args_one(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rectangle))

    def test_update_args_two(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rectangle))

    def test_update_args_three(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rectangle))

    def test_update_args_four(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rectangle))

    def test_update_args_five(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rectangle))


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rectangle))

    def test_update_kwargs_two(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rectangle))

    def test_update_kwargs_three(self):
        rectangle = Rectangle(10, 10, 10, 10, 10)
        rectangle.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rectangle))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_arg(self):
        rectangle = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rectangle.to_dictionary(1)
