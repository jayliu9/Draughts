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


def get_show_lst_by_actor(channel_lst, actor):
    '''
        Function -- get_show_lst_by_actor
            Searchs all channels for shows starring a particular actor.
        Parameters:
            channel_lst -- All available channels
            actor -- An Actor object
        Returns:
            The list of shows starring a partcular actor.
    '''
    show_lst = []
    for item in channel_lst:
        show_lst += item.get_shows_by_actor(actor)
    return show_lst


def get_channel_by_show(channel_lst, show):
    '''
        Function -- get_channel_by_show
            Gets channel information for a particular show.
        Parameters:
            channel_lst -- All available channels
            show -- An Show object
        Returns:
            The channel information for a particular show.
    '''
    WARNING = "No result"

    info = WARNING
    for channel in channel_lst:
        if channel.contains_show(show):
            info = channel.get_channel_info()
    return info


def get_shows_by_day(channel_lst, day):
    '''
        Function -- get_shows_by_day
            Gets all shows playing on a particular day across all channels.
        Parameters:
            channel_lst -- All available channels
            day -- An day of a week
        Returns:
            The list of all shows playing on a particular day across all
            channels.
    '''
    new_list = []
    for channel in channel_lst:
        if day in channel.schedule.keys():
            new_list += channel.schedule[day]
    return new_list


def main():
    actor1 = Actor("Actor", "1")
    actor2 = Actor("Actor", "2")
    actor3 = Actor("Actor", "3")
    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Tuesday Show", [actor1, actor2, actor3])
    show3 = Show("Friday Show", [actor2, actor3])
    schedule1 = {"Monday": [show1]}
    channel1 = Channel("DEF", 42, [show1], schedule1)
    schedule2 = {"Tuesday": [show2], "Friday": [show3]}
    channel2 = Channel("XYZ", 31, [show2, show3], schedule2)

    channels = [channel1, channel2]
    for item in get_show_lst_by_actor(channels, actor2):
        print(item.title)
    print("")
    print(get_channel_by_show(channels, show2))
    print("")
    for item in get_shows_by_day(channels, "Tuesday"):
        print(item.title)
 

if __name__ == "__main__":
    main()
