'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code enable a user to search their TV channels for shows based on criteria
of their choosing.
'''
from class_actor import Actor
from class_show import Show
from class_channel import Channel


def searcher(channel_lst, actor):
    show_lst = []
    for item in channel_lst:
        show_lst += item.get_shows_by_actor(actor)
    return show_lst


def main():
    actor1 = Actor("Actor", "1")
    actor2 = Actor("Actor", "2")
    actor3 = Actor("Actor", "3")
    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Tuesday Show", [actor1, actor2, actor3])
    show3 = Show("Friday Show", [actor2, actor3])
    channel1 = Channel("DEF", 42, [show1])
    channel2 = Channel("XYZ", 31, [show2, show3])

    channels = [channel1, channel2]



    print(searcher(channels, actor1))


if __name__ == "__main__":
    main()