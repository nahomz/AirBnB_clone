#!/usr/bin/python3
"""Module for Testing module place and class Place"""

from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
import pep8
import unittest


class TestPlace(unittest.TestCase):
    """Tests to Place class including docstrings and attributes"""
    @classmethod
    def setUpClass(cls):
        """Set up for Place class using unittest"""
        cls.place = Place()
        cls.place.city_id = "Nairobi"
        cls.place.user_id = "kulundeng"
        cls.place.name = "South Z"
        cls.place.description = "Great residential apartments"
        cls.place.number_rooms = 0
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 0
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_pep8_conformance_test_place(self):
        """Test that test_place.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_issubclass(self):
        """Test that Place is subclass of BaseModel class"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_class_docstring(self):
        """Test that Place has docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_class_public_attrs(self):
        """Test attributes of an instance of class Place"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_attrs_accept_only_strings(self):
        """Test that these attributes accept only str argumentst"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)

    def test_attrs_accept_int_only(self):
        """Test that these attributes accept only int arguments"""
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)

    def test_attrs_accept_float_only(self):
        """Test that thse attributes accept only floats arguments"""
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)

    def test_attrs_accept_list_only(self):
        """Test that these attributes accept only list arguments"""
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_save(self):
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.place), True)

if __name__ == "__main__":
    unittest.main()
