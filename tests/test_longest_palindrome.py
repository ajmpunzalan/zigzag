import unittest
from longest_palindrome import get_longest_palindrome


class TestLongestPalindrome(unittest.TestCase):
    def test_non_str_input(self):
        # TypeError should be raised for non string inputs
        self.assertRaises(TypeError, get_longest_palindrome, 1)
        self.assertRaises(TypeError, get_longest_palindrome, True)
        self.assertRaises(TypeError, get_longest_palindrome, ['string'])
        self.assertRaises(TypeError, get_longest_palindrome, None)

    def test_str_input(self):
        # No Execptions should be raised for string inputs
        try:
            get_longest_palindrome('this is not a palindrome')
        except TypeError as err:
            self.assertFalse(err)

    def test_longest_pal(self):
        # This should return the correct longest palindrom in a given string
        self.assertEqual(get_longest_palindrome('abaxyzzyxf'), 'xyzzyx')
        self.assertEqual(get_longest_palindrome('aaa'), 'aaa')
        self.assertEqual(get_longest_palindrome('abc'), 'a')
        self.assertEqual(get_longest_palindrome('123456789'), '1')

        # This returns True because our palindrome ignores non-alphanumeric characters
        self.assertEqual(get_longest_palindrome('abaxyz@!zyx@f'), 'xyz@!zyx@')
        self.assertEqual(get_longest_palindrome(
            '123A Santa Lived As a Devil At NASA!'), 'A Santa Lived As a Devil At NASA!')
