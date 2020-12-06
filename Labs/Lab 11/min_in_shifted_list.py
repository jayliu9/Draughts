'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is a function that finds the minimum in a shifted list.
'''


def find_min(shifted_lst):
    midpoint = len(shifted_lst) // 2
    left_lst = shifted_lst[:midpoint]
    right_lst = shifted_lst[midpoint:]

    if left_lst[0] <= left_lst[-1] and right_lst[0] <= right_lst[-1]:
        if shifted_lst[0] < shifted_lst[-1]:
            return shifted_lst[0]
        return shifted_lst[1]
    elif left_lst[0] > left_lst[-1]:
        return find_min(left_lst)
    else:
        return find_min(right_lst)
