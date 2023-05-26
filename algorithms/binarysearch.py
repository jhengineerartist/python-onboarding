class BinarySearch():
    """
    Binary search is an O(log n) search algorithm that finds an object in a sorted collection of comparable objects
    """
    def binary_search_iterative(item, sorted_lst):
        """
        Returns the index of the sought item in the provided sorted collection, or returns -1 if it is not found.

        This function performs the task using iterative conventions.

        Parameters:
        item (comparable): The comparable object to be searched for
        sorted_lst (collection): The sorted collection to be searched

        Returns:
        int: The index of the searched for object in the container or -1 if it is not found
        """
        found = False
        start = 0
        mid = 0
        end = len(sorted_lst)

        # Empty sets can't contain anything
        while (not found and start < end):
            mid = (start + end) // 2
            if (sorted_lst[mid] == item):
                found = True
            elif (item > sorted_lst[mid]):
                start = mid + 1
            else:
                end = mid

        return mid if found else -1

    def binary_search_recursive(item, sorted_lst):
        """
        Returns the index of the sought item in the provided sorted collection, or returns -1 if it is not found.

        This function performs the task using recursive conventions.

        Parameters:
        item (comparable): The comparable object to be searched for
        sorted_lst (collection): The sorted collection to be searched

        Returns:
        int: The index of the searched for object in the container or -1 if it is not found
        """
        end = len(sorted_lst)
        mid = 0 + end // 2
        item_position = -1
        if end == 1:
            item_position = 0 if sorted_lst[0] == item else -1
        elif end > 1:
            position_lower = BinarySearch.binary_search_recursive(
                item, sorted_lst[0:(mid - 1)])
            position_higher = BinarySearch.binary_search_recursive(
                item, sorted_lst[mid:end])

            # Add the mid back to position_higher since the output will be relative to the mid index
            position_higher = position_higher + mid if position_higher != -1 else -1

            # Default to the lower index so we pick the first found instance of the object.
            # If the item was not found in position_higher then will still assign -1 anyways since that's the base case
            item_position = position_lower if position_lower != -1 else position_higher
        return item_position
