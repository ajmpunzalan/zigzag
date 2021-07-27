import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_non_str_input(self):
        # TypeError should be raised for non string inputs
        self.assertRaises(TypeError, is_palindrome, 1)
        self.assertRaises(TypeError, is_palindrome, True)
        self.assertRaises(TypeError, is_palindrome, ['string'])
        self.assertRaises(TypeError, is_palindrome, None)

    def test_str_input(self):
        # No Execptions should be raised for string inputs
        try:
            is_palindrome('this is not a palindrome')
        except TypeError as err:
            self.assertFalse(err)

    def test_pal_str(self):
        # Test for palindrome strings
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('n   ur s e s      r u n   '))
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('abcdcba'))

        self.assertTrue(is_palindrome('123!!321@@@@'))
        self.assertTrue(is_palindrome('.@ - wow - @    .'))
        self.assertTrue(is_palindrome('~^$#@! . !@#$^~'))
        self.assertTrue(is_palindrome('!!!!asdsa!!!!'))

        self.assertTrue(is_palindrome('A Santa Lived As a Devil At NASA'))
        self.assertTrue(is_palindrome(
            'Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I DIet On Cod.'))

    def test_non_pal_str(self):
        # Test for palindrome strings
        self.assertFalse(is_palindrome('abc'))
        self.assertFalse(is_palindrome('I am a Palindrome'))
        self.assertFalse(is_palindrome('abaxyzzyxf'))


if __name__ == '__main__':
    unittest.main()
