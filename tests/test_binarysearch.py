import unittest
from algorithms.binarysearch import BinarySearch


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.sorted_int_list = [1, 2, 3, 4, 5]
        self.sorted_char_list = ['a', 'b', 'c', 'd', 'e']
        self.sorted_float_list = [1.1, 2.2, 3.3, 4.4, 5.5]

    def test_binary_search_iterative(self):
        # Affirmative case
        self.sorted_list_case(self.sorted_int_list, False)
        self.sorted_list_case(self.sorted_char_list, False)
        self.sorted_list_case(self.sorted_float_list, False)

        # Empty case
        output = BinarySearch.binary_search_iterative(0, [])
        self.assertEqual(output, -1)

        # Not found case
        output = BinarySearch.binary_search_iterative(6, self.sorted_int_list)
        self.assertEqual(output, -1)
        output = BinarySearch.binary_search_iterative(
            'z', self.sorted_char_list)
        self.assertEqual(output, -1)
        output = BinarySearch.binary_search_iterative(
            5.6, self.sorted_float_list)
        self.assertEqual(output, -1)

    def test_binary_search_recursive(self):
        # Affirmative case
        self.sorted_list_case(self.sorted_int_list, False)
        self.sorted_list_case(self.sorted_char_list, False)
        self.sorted_list_case(self.sorted_float_list, False)

        # Empty case
        output = BinarySearch.binary_search_recursive(0, [])
        self.assertEqual(output, -1)

        # Not found case
        output = BinarySearch.binary_search_recursive(6, self.sorted_int_list)
        self.assertEqual(output, -1)
        output = BinarySearch.binary_search_recursive(0, self.sorted_int_list)
        self.assertEqual(output, -1)
        output = BinarySearch.binary_search_recursive(
            'z', self.sorted_char_list)
        self.assertEqual(output, -1)
        output = BinarySearch.binary_search_recursive(
            5.6, self.sorted_float_list)
        self.assertEqual(output, -1)

    def sorted_list_case(self, sorted_list, use_recursive):
        list_length = len(sorted_list)
        for i in range(list_length):
            if use_recursive:
                binary_search_result = BinarySearch.binary_search_recursive(
                    sorted_list[i], sorted_list)
            else:
                binary_search_result = BinarySearch.binary_search_iterative(
                    sorted_list[i], sorted_list)
            self.assertEqual(i, binary_search_result)
