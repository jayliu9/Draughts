'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is a function that searches for the smallest integer in a
sorted list of integers which are shifted some unknown number of times.
'''


def search_for_min(shifted_lst):
    '''
        Function -- searches_for_min
            Searches for the smallest integer in a sorted list of
            integers which are shifted some unknown number of times.
        Parameters:
            shifted_lst -- The sorted-shifted list of integers to search in.
        Returns:
            The smallest integer in the sorted-shifted list.
    '''
    if shifted_lst[0] <= shifted_lst[-1]:
        return shifted_lst[0]
    midpoint = len(shifted_lst) // 2
    left_lst = shifted_lst[:midpoint]
    right_lst = shifted_lst[midpoint:]
    if shifted_lst[midpoint] > shifted_lst[-1]:
        return search_for_min(right_lst)
    elif shifted_lst[midpoint] < shifted_lst[midpoint - 1]:
        return shifted_lst[midpoint]
    return search_for_min(left_lst)
