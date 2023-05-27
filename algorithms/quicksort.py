class QuickSort():
    '''
    Quicksort is an O(n Log(n)) sort algorithm
    '''
    def quick_sort(unsorted_list):
        '''
        Given a list of items, returns a list of those items in a least to greatest sorted order

        Parameters:
        unsorted_list (comparable): The comparable object list to be sorted from least to greatest

        Returns:
        list (comparable): A list of the same items sorted from least to greatest
        '''
        sorted_list = unsorted_list.copy()
        # The base case will return a simple copy of the list if there is just one element or an empty list
        if len(sorted_list) > 1:
            pivot_point = len(sorted_list) // 2
            pivot_value = sorted_list[pivot_point]

            # Smaller values than the pivot go in the "left" list, larger values go in the "right" list.
            # We can ignore and pop the pivot value since that will go in between the left and right values and
            # should not be double counted
            left_list = []
            sorted_list.pop(pivot_point)
            right_list = []
            for item in sorted_list:
                if item <= pivot_value:
                    left_list.append(item)
                else:
                    right_list.append(item)

            # Recursively sort the two other sides around the pivot value
            left_list = QuickSort.quick_sort(left_list)
            right_list = QuickSort.quick_sort(right_list)

            # The sorted list is now the concatenated set of the sorted lesser values, the pivot value, and the greater values
            left_list.append(pivot_value)
            sorted_list = left_list + right_list
        return sorted_list
