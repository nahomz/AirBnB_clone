#!/usr/bin/python3
"""Module for Testing module place and class Amenity"""

from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8
import unittest


class TestAmenity(unittest.TestCase):
    """Tests to Amenity class including docstrings and attributes"""
    @classmethod
    def setUpClass(cls):
        """Set up for Amenity class using unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "swimming pool"

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_pep8_conformance_test_amenity(self):
        """Test that test_amenity.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_issubclass(self):
        """Test that Amenity is subclass of BaseModel class"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_class_docstring(self):
        """Test that Amenity has docstring"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_class_public_attrs(self):
        """Test attributes of an instance of class Amenity"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attrs_accept_only_strings(self):
        """Test that these attributes accept only str argumentst"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save(self):
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity), True)

if __name__ == "__main__":
    unittest.main()
