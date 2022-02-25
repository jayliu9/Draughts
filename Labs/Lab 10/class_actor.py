'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is an actor class
'''


class Actor:
    '''
        Class -- Actor
            Represents an actor.
        Attributes:
            lastname -- The last name of the actor.
            firstname -- The first name of the actor.
    '''

    def __init__(self, firstname, lastname):
        '''
            Constructor -- __init__
                Creates a new instance of Actor
            Parameters:
                self -- The current Actor object
                firstname -- The first name of the actor
                lastname -- The last name of the actor
        '''
        self.firstname = firstname
        self.lastname = lastname
