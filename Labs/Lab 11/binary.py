'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is a recursive function of binary search.
'''


def binary_search(lst, item):
    '''
        Function -- binary_search
            Searches for the given item in the given list.
        Parameters:
            lst -- The list to search in.
            item -- The item to search for.
        Returns:
            True if item is in lst, False otherwise.
    '''
    midpoint = len(lst) // 2
    left_half = lst[:midpoint]
    right_half = lst[midpoint + 1:]
    if is_empty_lst(lst):
        return False
    elif lst[midpoint] == item:
        return True
    elif lst[midpoint] > item:
        return binary_search(left_half, item)
    return binary_search(right_half, item)


def is_empty_lst(lst):
    '''
        Function -- is_empty_lst
            Checks if the given list is empty.
        Parameters:
            lst -- The list to check.
        Returns:
            True if the list is empty, False otherwise.
    '''
    return len(lst) == 0