'''
The code is piece class.
'''


class Piece:
    '''
        Class -- Piece
            A piece.
        Attributes:
            color -- The color of the piece.
            directions -- The directions the piece can move in
            is_king -- Whether or not the piece is a king.
        Methods:
            initialize_direction -- Helper method to initialize the direction
            the piece can move in
            become_king -- Upgrades the piece to the king piece
    '''
    def __init__(self, color):
        '''
            Constructor -- Creates a new instance of Piece
            Parameters:
                self -- The current Piece object.
                color -- The color of the piece.
        '''
        self.color = color
        self.initialize_direction()
        self.is_king = False

    def initialize_direction(self):
        '''
            Method -- initialize_direction
                Helper method to initialize the direction the piece can move in
            Parameter:
                self -- The current Piece object.
        '''
        BLACK = 0
        RED = 1
        B_RGL_DIRECTION = [[1, -1], [1, 1]]
        R_RGL_DIRECTION = [[-1, -1], [-1, 1]]

        if self.color == BLACK:
            self.directions = B_RGL_DIRECTION
        else:
            self.directions = R_RGL_DIRECTION

    def become_king(self):
        '''
            Method -- become_king
                Upgrades the piece to the king piece
            Parameter:
                self -- The current Piece object.
        '''
        KING_DIRECTION = [[1, -1], [1, 1], [-1, -1], [-1, 1]]

        self.directions = KING_DIRECTION
        self.is_king = True

    def __eq__(self, other):
        '''
            Method -- __eq__
                Checks if two Piece objects are equal
            Parameters:
                self -- The current Piece object
                other -- An object to compare self to.
            Returns:
                True if the two objects are equal, False otherwise.
        '''
        if type(self) != type(other):
            return False
        return self.color == other.color and self.is_king == other.is_king
