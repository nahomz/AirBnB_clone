#!/usr/bin/python3
"""Module for Testing module review and class Review"""

from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
import pep8
import unittest


class TestREview(unittest.TestCase):
    """Tests to Review class including docstrings and attributes"""
    @classmethod
    def setUpClass(cls):
        """Set up for Review class using unittest"""
        cls.review = Review()
        cls.review.place_id = "NRB"
        cls.review.user_id = "kulundeng"
        cls.review.text = "This place has fleas please beware"

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_pep8_conformance_test_review(self):
        """Test that test_review.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_issubclass(self):
        """Test that Review is subclass of BaseModel class"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_class_docstring(self):
        """Test that Review has docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_class_public_attrs(self):
        """Test attributes of an instance of class Review"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_attrs_accept_only_strings(self):
        """Test that these attributes accept only str argumentst"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.review), True)

if __name__ == "__main__":
    unittest.main()
