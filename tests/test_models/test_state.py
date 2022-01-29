#!/usr/bin/python3
"""Module for Testing module  State and class State"""

from datetime import datetime
from models.state import State
from models.base_model import BaseModel
import pep8
import unittest


class TestState(unittest.TestCase):
    """Tests to State class including docstrings and attributes"""
    @classmethod
    def setUpClass(cls):
        """Set up class instance for tests"""
        cls.state = State()
        cls.state.name = "Tom Mboya"

    def test_pep8_conformance_state(self):
        """Test that models/state.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_pep8_conformance_test_state(self):
        """Test that test_state.py conforms to PEP8 standardization."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or/and warnings.")

    def test_issubclass(self):
        """Test that State is subclass of BaseModel class"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_class_docstring(self):
        """Test that State has docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_class_public_attrs(self):
        """Test attributes of an instance of class State"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_attrs_accept_only_strings(self):
        """Test that these attributes accept only str arguments"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.state), True)

if __name__ == "__main__":
    unittest.main()
