#!/usr/bin/python3
"""Module for Testing module place and class Place"""

from datetime import datetime
from models.city import City
from models.base_model import BaseModel
import pep8
import unittest


class TestCity(unittest.TestCase):
    """Tests to City class including docstrings and attributes"""
    @classmethod
    def setUpClass(cls):
        """Set up for City class unittest"""
        cls.city = City()
        cls.city.name = "Nairobi"
        cls.city.state_id = "NRB"

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_pep8_conformance_test_city(self):
        """Test that test_city.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_issubclass(self):
        """Test that City is subclass of BaseModel class"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_class_docstring(self):
        """Test that City has docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_class_public_attrs(self):
        """Test attributes of an instance of class City"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attrs_accept_only_strings(self):
        """Test that these attributes accept only str argumentst"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.city), True)

if __name__ == "__main__":
    unittest.main()
