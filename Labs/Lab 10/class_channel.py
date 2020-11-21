'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is a channel class
'''


class Channel:
    def __init__(self, name, number, shows):
        self.name = name
        self.number = number
        self.shows = shows

    def get_shows_by_actor(self, actor):
        new_list = []
        for each in self.shows:
            if each.contains_actor(actor):
                new_list.append(each.title)
        return new_list
