import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_finds_target(self):
        numbers = [2, 5, 8, 12, 16]
        result = binary_search(numbers, 12)
        self.assertEqual(result, 3)
    def test_target_not_found(self):
        self.assertEqual(binary_search([2, 5, 8, 12, 16], 7), -1)
    def test_single_item_list(self):
        self.assertEqual(binary_search([4], 4), 0)
    def test_empty_list(self):
        self.assertEqual(binary_search([], 4), -1)
    def test_first_element(self):
        self.assertEqual(binary_search([2, 5, 8, 12, 16], 2), 0)

if __name__ == "__main__":
    unittest.main()