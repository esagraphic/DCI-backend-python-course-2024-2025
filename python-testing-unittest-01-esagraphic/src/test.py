from text import to_upper, to_word_list_isupper
import unittest

    
class TestUppercase(unittest.TestCase):

    def test_upper_case(self):
        self.assertEqual(to_upper("abcdef"),"ABCDEF")

    def test_if_all_is_upper_and_true(self):
        self.assertTrue(to_word_list_isupper(['I', 'LOVE', 'YOU']))

    def test_if_all_is_upper_and_false(self):
        self.assertFalse(to_word_list_isupper(['i', 'LOVE', 'YOU']))

    def test_to_upper_Typeerror(self):
        with self.assertRaises(TypeError):
            to_upper(666)

    def test_to_isupper_Typeerror(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper('I love you')

if __name__ == '__main__':
    unittest.main()