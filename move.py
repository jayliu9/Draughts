'''
The code is move class.
'''


class Move:
    '''
        Class -- Move
            A move.
        Attributes:
            start -- The location of the square containing the piece at the
            beginning of the move.
            end -- The location of the square that the moved piece ends up in.
            is_capt -- Whether or not it is a capturing move.
    '''

    def __init__(self, start, end, is_capt):
        '''
            Constructor -- Creates a new instance of Move
            Parameters:
                self -- The current Move object.
                start -- The location of the square containing the piece at the
                beginning of the move
                end -- The location of the square that the moved piece ends up
                in.
                is_capt -- Whether or not it is a capturing move.
        '''
        self.start = start
        self.end = end
        self.is_capt = is_capt

    def __eq__(self, other):
        '''
            Method -- __eq__
                Checks if two Move objects are equal
            Parameters:
                self -- The current Move object
                other -- An object to compare self to.
            Returns:
                True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return (self.start == other.start and self.end == other.end and
                self.is_capt == other.is_capt)
