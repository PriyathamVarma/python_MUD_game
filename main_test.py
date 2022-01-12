""" This file conatins all test cases for functions"""


from main import *
from new import *
from info import *
from Characters import *
from Objects import *
from Castles import *
from Castles_Weapons_Selection import *

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
    # test for castle weapons selection
    def test_castle1(self):
        self.assertTrue(castle_1_weapon_selection) 
    def test_castle2(self):
        self.assertTrue(castle_2_weapon_selection)
    def test_castle3(self):
        self.assertTrue(castle_3_weapon_selection)      


        