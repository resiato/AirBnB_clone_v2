#!/usr/bin/python3
"""test for databasse storage"""
import unittest
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import MySQLdb
import pep8


class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            cls.db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                     getenv("HBNB_MYSQL_USER"),
                                     getenv("HBNB_MYSQL_PWD"),
                                     getenv("HBNB_MYSQL_DB"))
            cls.cursor = cls.db.cursor()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db.close()

    def test_pep8_DBStorage(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes_DBStorage(self):
        """Tests for class attributes"""
        # self.assertTrue(hasattr(DBStorage, '__engine'))
        # self.assertTrue(hasattr(DBStorage, '__session'))


