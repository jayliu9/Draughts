'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is a show class
'''


class Show:
    '''
        Class -- Show
            Represents a show.
        Attributes:
            title -- The title of the show.
            members -- The cast members of the show.
    '''
    def __init__(self, title, members):
        '''
            Constructor -- __init__
                Creates a new instance of Show
            Parameters:
                self -- The current Show object
                title -- The title of the show.
                members -- The cast members of the show.
        '''
        self.title = title
        self.members = members

    def contains_actor(self, actor):
        '''
            Method -- contains_actor
                Checks if the given actor is in the show's cast list.
            Parameter:
                self -- The current Show object
                actor -- An Actor object
            Returns:
                True if the actor is in the show's cast list, False otherwise.
        '''
        return actor in self.members