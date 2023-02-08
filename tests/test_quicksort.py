import unittest
import sys
sys.path.insert(0, './src')
from quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        quick_sort(arr, 0, 0)
        self.assertEqual(arr, [])

    def test_array_of_length_one(self):
        arr = [1]
        quick_sort(arr, 0, 0)
        self.assertEqual(arr, [1])

    def test_array_of_length_two(self):
        arr = [2, 1]
        quick_sort(arr, 0, 1)
        self.assertEqual(arr, [1, 2])

    def test_array_of_length_three(self):
        arr = [2, 1, 3]
        quick_sort(arr, 0, 2)
        self.assertEqual(arr, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
