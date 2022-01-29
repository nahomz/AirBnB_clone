#!/usr/bin/python3

import unittest
import pep8
import os
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ Test user module and User class"""
    @classmethod
    def setUpClass(cls):
        """set up class instance"""
        cls.u = User()
        cls.u.first_name = "Charles"
        cls.u.last_name = "Osoti"
        cls.u.email = "icampusvillage@gmail.com"
        cls.u.password = "otitmach"

    def test_pep8_conformance_user(self):
        """Test that user.py follows PEP8 practices"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors and/or warnings.")

    def test_pep8_conformance_test_user(self):
        """Test that test_user.py follows PEP8 practices"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors and/or warnings.")

    def test_user_docstring(self):
        """Test for user module docstring"""
        self.assertIsNot(User.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(User.__doc__) > 0,
                        "user.py needs a docstring")

    def test_user_attrs(self):
        """Test that all public attributes of user exists"""
        self.assertTrue('id' in self.u.__dict__)
        self.assertTrue('first_name' in self.u.__dict__)
        self.assertTrue('last_name' in self.u.__dict__)
        self.assertTrue('email' in self.u.__dict__)
        self.assertTrue('created_at' in self.u.__dict__)
        self.assertTrue('updated_at' in self.u.__dict__)
        self.assertTrue('password' in self.u.__dict__)

    def test_attributes_type_is_string(self):
        """Test that attributes accepts strings"""
        self.assertEqual(type(self.u.email), str)
        self.assertEqual(type(self.u.password), str)
        self.assertEqual(type(self.u.first_name), str)
        self.assertEqual(type(self.u.last_name), str)

if __name__ == "__main__":
    unittest.main()
