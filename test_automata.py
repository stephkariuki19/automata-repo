import unittest
from unittest import TestCase
from unittest.mock import patch
#how to import whole file?
from automata import *

# from automata import pickLanguage
# from automata import language_one
# from automata import language_two


class Test(TestCase):
    def test_pick_language_two(self):
        self.assertEqual(pickLanguage("L2"),language_two())

    def test_pick_language_one(self):
        self.assertEqual(pickLanguage("L1"),language_one())
    def test_language_input(self):
        self.assertRaises(wrongLanguageError,pickLanguage,1)

    def test_invalidAlphabet(self,mock_language_one):
        alpha_one = "a"
        alpha_two = "b"
        example_input = alpha_one + alpha_two + "s"

        #self.assertRaises(KeyError,processString,example_input)
    #def test_wrong_language(self):
        #self.assertEqual(pickLanguage("m"),"wrong language")
    #def language_one_transition(self):
       # self.assertEqual(transition_function[(D, alpha_one)] ="D")



# class Test(TestCase):
#     def test_language_two(self):
#         self.fail()

if __name__ == '__main__':
    unittest.main()

