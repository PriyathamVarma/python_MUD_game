from Play import *
import unittest

class TestPlay(unittest.TestCase):

    def test_play(self):
        self.assertTrue(Play("varma","kings","kings"))
