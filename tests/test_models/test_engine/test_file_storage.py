#!/usr/bin/python3
""" module for FileStorage class unittest"""

import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    """cls for Testing FileStorage Clasds"""

    @classmethod
    def setUpClass(cls):
        """set up class for tests"""
        cls.u = User()
        cls.u.first_name = "Victor"
        cls.u.last_name = "Benosa"
        cls.u.email = "icampusvvillage@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """tear down the class instance after test"""
        del cls.u

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors and/or warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files([
            'tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors and/or warnings).")

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        os.remove("file.json")
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_private_attributes(self):
        """Test that all private attributes are private."""
        fstorage = FileStorage()
        with self.assertRaises(AttributeError):
            print(fstorage.objects)
        with self.assertRaises(AttributeError):
            print(fstorage.file_path)

    def test_working_reload(self):
        """Test that reload method works."""
        base = BaseModel()
        key = "BaseModel" + "." + base.id
        base.save()
        base1 = BaseModel()
        key1 = "BaseModel" + "." + base1.id
        base1.save()
        self.assertTrue(storage.all()[key] is not None)
        self.assertTrue(storage.all()[key1] is not None)
        with self.assertRaises(KeyError):
            storage.all()["benosa"]
