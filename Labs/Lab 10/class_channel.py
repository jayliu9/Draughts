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
            Parameters:
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

    def contains_show(self, show):
        '''
            Method -- contains_show
                Checks if the given show is broadcast on the channel.
            Parameters:
                self -- The current Channel object
                actor -- An Show object
            Returns:
                True if the show is broadcast on the channel, False otherwise.
        '''
        return show in self.shows

    def get_channel_info(self):
        '''
            Method -- get_channel_info
                Gets the information of the channel.
            Parameters:
                self -- The current Channel object
            Returns:
                The information of the channel.
        '''
        SUBTITLE = "Channel information: "
        NAME = "Name: "
        NUMBER = "Number: "
        SHOWS = "Shows: "
        NEW_LINE = "\n"
        show_lst = []
        for show in self.shows:
            show_lst.append(show.title)

        msg = (SUBTITLE + NEW_LINE + NAME + self.name + NEW_LINE + NUMBER +
               str(self.number) + NEW_LINE + SHOWS + str(show_lst))
        return msg
               
        
        
