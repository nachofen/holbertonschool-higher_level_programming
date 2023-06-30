#!/usr/bin/python3
"""Testing Base"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    """Unittests for testing the init of base class"""

    def test_no_args(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_None(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_unique(self):
        self.assertEqual(12, Base(12).id)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_id_type_str(self):
        self.assertEqual("test", Base("test").id)

    def test_id_type_float(self):
        self.assertEqual(1.2, Base(1.2).id)

    def test_id_type_dict(self):
        self.assertEqual({"test1": 1, "test2": 2},
                         Base({"test1": 1, "test2": 2}).id)

    def test_id_type_tup(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_id_type_list(self):
        self.assertEqual([1, 2], Base([1, 2]).id)

    def test_id_type_bool(self):
        self.assertEqual(False, Base(False).id)

    def test_id_type_set(self):
        self.assertEqual({"a", "b"}, Base({"a", "b"}).id)

    def test_id_type_inf(self):
        self.assertEqual(float("inf"), Base(float("inf")).id)

    def test_id_type_Nan(self):
        self.assertNotEqual(float("Nan"), Base(float("Nan")).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class"""
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""
    def test_save_to_file_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        full = '[{"y": 8, "x": 2, "id": 5, "width": 10, "height": 7}]'
        correct_len = len(full)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == correct_len)

    def test_save_to_file_square(self):
        r = Square(10, 2, 8, 5)
        full = '[{"y": 8, "x": 2, "id": 5, "size": 10}]'
        correct_len = len(full)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == correct_len)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])

    def test_dif_objs(self):
        r = Rectangle(10, 2, 3, 8, 5)
        s = Square(10, 2, 8, 5)
        objs_list = [r, s]
        Base.save_to_file(objs_list)
        with open("Base.json", "r") as f:
            file_contents = f.read()
            self.assertIn('"height": 2, "width": 10', file_contents)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""
    def test_from_json_string_type(self):
        my_list = [{"id": 89, "width": 10, "height": 4}]
        json_list = Rectangle.to_json_string(my_list)
        back_list = Rectangle.from_json_string(json_list)
        self.assertEqual(list, type(back_list))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string(2, 1)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of base class"""
    def test_load_from_file_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        output_list = Rectangle.load_from_file()
        self.assertEqual(str(r), str(output_list[0]))

    def test_load_from_file_square(self):
        s = Square(5, 1, 3, 3)
        Square.save_to_file([s])
        output_list = Square.load_from_file()
        self.assertEqual(str(s), str(output_list[0]))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 2)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of base class"""
    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is_same(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        r1 = Square(3, 5, 1, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(r2))

    def test_create_square_is_same(self):
        r1 = Square(3, 5, 1, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_equals(self):
        r1 = Square(3, 5, 1, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
