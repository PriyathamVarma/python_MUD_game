""" This file conatins all test cases for functions"""


from main import *
from new import *
from info import *
from Characters import *
from Objects import *
from Castles import *

import unittest

class TestMain(unittest.TestCase):
    # test for main
    def test_main(self):
        self.assertTrue(start)
    # test for new
    def test_new(self):
        self.assertTrue(new)    
    # test for info
    def test_info(self):
        self.assertTrue(info) 
    # test for castles
    def test_castles(self):
        self.assertTrue(castle)
    # test for characters
    def test_characters(self):
        self.assertTrue(characters)    
    # test for objects
    def test_objects(self):
        self.assertTrue(objects) 