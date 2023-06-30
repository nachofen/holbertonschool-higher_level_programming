#!/usr/bin/python3
"""unittests for square"""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_init(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class"""

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)

    def test_two_args(self):
        r1 = Square(10)
        r2 = Square(10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_size_getter(self):
        s = Square(5, 7, 5, 1)
        self.assertEqual(5, s.size)

    def test_size_setter(self):
        s = Square(5, 7, 5, 1)
        s.size = 10
        self.assertEqual(10, s.size)

    def test_x_getter(self):
        s = Square(7, 7, 5, 1)
        self.assertEqual(7, s.x)

    def test_x_setter(self):
        s = Square(5, 7, 5, 1)
        s.x = 10
        self.assertEqual(10, s.x)

    def test_y_getter(self):
        s = Square(5, 7, 5, 1)
        self.assertEqual(5, s.y)

    def test_y_setter(self):
        s = Square(5, 7, 5, 1)
        s.y = 10
        self.assertEqual(10, s.y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.14)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([5.5, 2])

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 5.5, "b": 2})

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "string")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 3.14)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [5.5, 2])

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"a": 5.5, "b": 2})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, False)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2, 3))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('nan'))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -5)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, "string")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, 3.14)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, [5.5, 2])

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, {"a": 5.5, "b": 2})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, False)

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, (1, 2, 3))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 3, -5)


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_small_size(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large_size(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the square class"""

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(8)
        self.assertEqual("[Square] (8) 10/10 - 10", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(8, 2, 4, 5)
        self.assertEqual("[Square] (8) 4/5 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(9, 2, 4, 5, 7)
        self.assertEqual("[Square] (9) 4/5 - 2", str(s))

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(1, 1, 1, 1)
        s.update(9, 2, 4, 5)
        s.update(6, 5, 3, 2)
        self.assertEqual("[Square] (6) 3/2 - 5", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(1, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(1, -5)

    def test_update_args_invalid_x_type(self):
        s = Square(1, 10, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(8, 2, "string")

    def test_update_args_x_negative(self):
        s = Square(1, 1, 10, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(9, 1, -6)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(8, 3, 4, "text")

    def test_update_args_y_negative(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(8, 1, 3, -6)


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the square class."""

    def test_update_kwargs_None_id(self):
        s = Square(1, 1, 1, 1)
        s.update(id=None)
        correct = "[Square] ({}) 1/1 - 1".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_one(self):
        s = Square(1, 1, 1, 1)
        s.update(id=1)
        self.assertEqual("[Square] (1) 1/1 - 1", str(s))

    def test_update_kwargs_five(self):
        s = Square(2, 2, 2, 2)
        s.update(y=5, x=8, id=9, size=1)
        self.assertEqual("[Square] (9) 8/5 - 1", str(s))

    def test_update_kwargs_twice(self):
        s = Square(2, 2, 1, 1)
        s.update(id=9, x=1)
        s.update(y=3, size=2)
        self.assertEqual("[Square] (9) 1/3 - 2", str(s))

    def test_update_kwargs_invalid_size_type(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="str")

    def test_update_kwargs_size_zero(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_kwargs_inavlid_x_type(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="str")

    def test_update_kwargs_x_negative(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="no int")

    def test_update_kwargs_y_negative(self):
        s = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(8, 2, y=26)
        self.assertEqual("[Square] (8) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(z=1, j=2)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_some_good_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=8, a=12, b=4, x=1, y=7)
        self.assertEqual("[Square] (8) 1/7 - 5", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the square class."""

    def test_to_dictionary_output(self):
        s = Square(2, 3, 11, 1)
        correct = {'x': 3, 'y': 11, 'id': 1, 'size': 2}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_one_arg(self):
        s = Square(2, 4, 1, 2)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)
