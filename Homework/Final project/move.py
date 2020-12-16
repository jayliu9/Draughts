'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is move class.
'''


class Move:
    '''
        Class -- Move
            The move.
        Attributes:
            start -- The location of the square containing the piece at the
            beginning of the move.
            end -- The location of the square that the moved piece ends up in.
            is_capt -- Whether or not it is a capturing move.
    '''

    def __init__(self, start, end, is_capt):
        self.start = start
        self.end = end
        self.is_capt = is_capt
