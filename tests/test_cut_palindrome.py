import unittest
from cut_palindrome import cut_palindrome


class TestCutPalindrome(unittest.TestCase):
    def test_non_str_input(self):
        # TypeError should be raised for non string inputs
        self.assertRaises(TypeError, cut_palindrome, 1)
        self.assertRaises(TypeError, cut_palindrome, True)
        self.assertRaises(TypeError, cut_palindrome, ['string'])
        self.assertRaises(TypeError, cut_palindrome, None)

    def test_str_input(self):
        # No Execptions should be raised for string inputs
        try:
            cut_palindrome('this is not a palindrome')
        except TypeError as err:
            self.assertFalse(err)

    def test_num_cuts(self):
        # Check whether the returned value of the function is correct
        self.assertEqual(cut_palindrome('noonabbad'), 2)
        self.assertEqual(cut_palindrome('noonabcbadnoon'), 3)
        self.assertEqual(cut_palindrome('A Santa Lived As a Devil At NASA'), 0)
        self.assertEqual(cut_palindrome('abcnurses run papi'), 5)
        self.assertEqual(cut_palindrome('abcde'), 4)
