import unittest
from algorithms.selectionsort import SelectionSort


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.int_array = [-1, 123, 3, 45, -51]
        self.int_array_sorted = [-51, -1, 3, 45, 123]
        self.char_array = ['b', 'y', 'c', 'j']
        self.char_array_sorted = ['b', 'c', 'j', 'y']

    def test_selection_sort(self):
        # Affirmative cases
        self.assertEqual(self.int_array_sorted,
                         SelectionSort.selection_sort(self.int_array))
        self.assertEqual(self.char_array_sorted,
                         SelectionSort.selection_sort(self.char_array))

        # Empty case
        self.assertEqual([], SelectionSort.selection_sort([]))
