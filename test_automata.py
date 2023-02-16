import unittest
from unittest import TestCase
from automata import *


class Test(TestCase):
    def test_pick_language_two(self):
        self.assertEqual(pickLanguage("L2"), language_two())

    def test_pick_language_one(self):
        self.assertEqual(pickLanguage("L1"), language_one())

    def test_language_input(self):
        self.assertRaises(wrongLanguageError, pickLanguage, 1)

    def test_invalidAlphabet(self):
        alpha_one = "a"
        alpha_two = "b"
        self.assertRaises(KeyError, checkAlphabets,alpha_one,alpha_two,"s")
    def test_emptyString(self):
        self.assertRaises(ValueError,checkIfEmpty,"")


if __name__ == '__main__':
    unittest.main()




