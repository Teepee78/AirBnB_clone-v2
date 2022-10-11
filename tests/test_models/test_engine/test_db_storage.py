#!usr/bin/python3
"""
Module that tests the db_storage
"""
import unittest
import MySQLdb
from sqlalchemy import create_engine
from os import getenv
# Importing objects
from models.state import State
from models.engine.db_storage import DBStorage

class test_DBStorage(unittest.TestCase):
    """ Class to test the database storage method """
    
    storage = DBStorage()
    # Setting up storage
    storage.reload()
    state_obj2 = State()
    state_obj = State()

    def setUp(self):
        """ Set up test environment """
        self.db = MySQLdb.connect(host=getenv("HBNB_MYSQL_HOST", default=None), port=3306,\
                             user=getenv("HBNB_MYSQL_USER", default=None),\
                             passwd=getenv("HBNB_MYSQL_PWD", default=None),\
                             db=getenv("HBNB_MYSQL_DB", default=None))
        self.cur = self.db.cursor() 

    def tearDown(self):
        """ Tear down test environmet """
    

    def test_new(self):
        """ Test the new method """ 
        # Creating an object and adding to session
        self.state_obj2.name = "California" 

        # Getting all elements in database before adding to session
        elem_orm_before = self.storage.all("State")
        self.storage.new(self.state_obj2)
        self.storage.save()
        
        # Getting all elements in database after adding to session
        elem_orm_after = self.storage.all("State")
        self.assertEqual((len(elem_orm_before) + 1), len(elem_orm_after))


    def test_all(self):
        """" Test the all method """ 
        # Setting up storage
        # self.storage.reload()
        # Creating an object and saving
        self.state_obj.name = "California"
        self.state_obj.save()

        # Retrieving all State objects from Database using ORM
        elem_orm = self.storage.all("State")

        # Retriveing all State objects from Database using mysqldb
        elem_mysqldb = self.cur.execute("SELECT * FROM states")
        self.assertEqual(elem_mysqldb, len(elem_orm))        

    def test_save(self):
        """ Test the save method """

    def test_delete(self):
        """ Test the delete method """

    def test_reload(self):
        """ Test the reload method """

    def test_PEP8(self):
        """ Test PEP8 requirements """
