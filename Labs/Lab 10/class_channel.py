'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is a channel class
'''


class Channel:
    '''
        Class -- Channel
            Represents a channel.
        Attributes:
            name -- The name of the channel.
            number -- The number of the channel.
            shows -- The shows broadcast on the channel.
    '''

    def __init__(self, name, number, shows):
        '''
            Constructor -- __init__
                Creates a new instance of Actor
            Parameters:
                self -- The current Channel object
                name -- The name of the channel.
                number -- The number of the channel.
                shows -- The shows broadcast on the channel.
        '''
        self.name = name
        self.number = number
        self.shows = shows

    def get_shows_by_actor(self, actor):
        '''
            Method -- get_shows_by_actor
                Gets the list of shows broadcast on the channel which starring
                the given actor. 
            Parameter:
                self -- The current Channel object
                actor -- An Actor object
            Returns:
                The list of shows broadcast on the channel which starring the
                given actor.
        '''
        new_list = []
        for each in self.shows:
            if each.contains_actor(actor):
                new_list.append(each.title)
        return new_list
