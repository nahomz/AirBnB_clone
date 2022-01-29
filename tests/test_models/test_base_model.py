#!/usr/bin/python3
""" unittest for BaseModel class"""
from time import sleep
import pep8
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for base_model module and BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """ set up base class"""
        cls.base = BaseModel()

    @classmethod
    def teardown(cls):
        del cls.base

    # test pep8 conformation
    def test_pep8_conformance_base_model(self):
        """ Test that base_model.py follows pep8 standardization"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or warnings")

    def test_pep8_conformance_test_base_model(self):
        """ Test that test_base_model.py follows pep8 standardization"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or warnings")

    def test_save(self):
        """Test public method save() for class BaseModel"""
        base1 = BaseModel()
        initial_time = base1.updated_at
        sleep(0.5)
        base1.save()
        updated_time = base1.updated_at
        self.assertNotEqual(initial_time, updated_time)

    def test_to_dict(self):
        """Test that to_dict() creates a dictionary object of an instance"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
