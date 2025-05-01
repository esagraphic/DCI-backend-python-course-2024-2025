# src/test.py

import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):

    # Task 1: Test if rnd returns a number within the correct range
    def test_rnd_correct_value(self):
        result = rnd(2, 20)
        # The test assumes the random function always returns a value within the correct range.
        self.assertGreaterEqual(result, 2, "The random number is less than the start value.")
        self.assertLessEqual(result, 20, "The random number is greater than the end value.")

    # Task 2: Test if rnd does not return an out-of-range value
    def test_rnd_out_of_range(self):
        result = rnd(2, 20)
        # Randomness can make tests unreliable, but this test checks if the number is in range.
        self.assertTrue(2 <= result <= 20, "The random number is out of range.")

    # Task 4: Test if max_num_in_list returns the highest number
    def test_max_num_in_list(self):
        result = max_num_in_list([2, 6, 8, 7, -1])
        self.assertEqual(result, 8, "The returned value is not the greatest value in the list.")

    # Additional test to check if max_num_in_list raises an exception for an empty list
    def test_max_num_in_list_empty(self):
        with self.assertRaises(ValueError, msg="The list is empty"):
            max_num_in_list([])

if __name__ == '__main__':
    unittest.main()
