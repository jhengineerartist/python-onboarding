
class SelectionSort():
    '''
    Selection sort is an O(n^2) sorting algorithm
    '''
    def selection_sort(unsorted_list):
        '''
        Given a list of items, returns a list of those items in a least to greatest sorted order

        Parameters:
        unsorted_list (comparable): The comparable object list to be sorted from least to greatest

        Returns:
        list (comparable): A list of the same items sorted from least to greatest
        '''
        # Copy the contents of list into sorted_list so that
        # we maintain the same data type and size
        sorted_list = unsorted_list.copy()
        exc_set = set()

        for i in range(len(unsorted_list)):
            smallest_index, exc_set = SelectionSort.find_smallest(
                unsorted_list, exc_set)
            sorted_list[i] = unsorted_list[smallest_index]

        return sorted_list

    def find_smallest(list, exc_set):
        '''
        Given a list of items and indices to ignore, returns the smallest item in the list not including those items in the indices to ignore

        Parameters:
        list (comparable): The comparable object list to be sorted from least to greatest

        Returns:
        list (comparable): A list of the same items sorted from least to greatest
        '''
        smallest_index = -1
        smallest = None

        for i in range(len(list)):
            if i not in exc_set and (smallest is None or list[i] <= smallest):
                smallest = list[i]
                smallest_index = i

        exc_set.add(smallest_index)
        return smallest_index, exc_set
