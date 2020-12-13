'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for making a Facebook just for the Seven Dwarves.
'''


def read_file(path):
    '''
        Function -- read_file
            Reads a file.
        Parameters:
            path -- A string file path
        Returns:
            The contents in the file as a list of strings.
    '''
    lines = []
    try:
        with open(path, "r") as file:
            for line in file:
                lines.append(line)
    except FileNotFoundError:
        print("File not found")
    return lines


def create_network(lines):
    '''
        Function -- create_network
            Uses a dictionary to represent the network populated from text file
        Parameters:
            lines -- The contents in the text file.
        Returns:
            The dictionary representing the network.
    '''
    network = {}
    for line in lines:
        processed_line = line_processing(line)
        network[processed_line[0]] = processed_line[1:]
    return network


def line_processing(line):
    '''
        Function -- line_processing
            Removes leading or trailing whitespace from a line and splits the
            string of dwarves' names into a list using any whitespace
        Parameters:
            line -- A line of dwarves' names in text file.
        Returns:
            The list containing dwarves' names in a line.
    '''
    return line.split()


def generate_line(key, dic):
    '''
        Function -- generate_line
            Generates a string as a line of the text file from a dictionary
            item based on the original format.
        Parameters:
            key -- The key of the dictionary item
            dic -- The dictionary
        Returns:
            A string as a line of the text file in required format
    '''
    WHITESPACE = " "
    return key + WHITESPACE + WHITESPACE.join(dic[key])


def generate_text(network_dic):
    '''
        Function -- generate_line
            Generates a list of the whole network in the original format from
            the dictionary of the network.
        Parameters:
            network_dic -- The dictionary of the network.
        Returns:
            The list of the whole network in the original format.
    '''
    text_lines = []
    for key in network_dic:
        line = generate_line(key, network_dic)
        text_lines.append(line)
    return text_lines


def write_file(path, content):
    '''
        Function -- write_file
            Writes a text into a file.
        Parameters:
            path -- A string file path
            content -- A list of content to write
        Returns:
            None. This function does not return.
    '''
    with open(path, "w") as file:
        for line in content:
            file.write(line + "\n")


def unfriending(subject_dwarf, object_dwarf, network):
    '''
        Function -- unfriending
            Unfriends someone.
        Parameters:
            subject_dwarf -- The dwarf who unfriends someone.
            object_dwarf -- The dwarf to unfriend
            network -- The dictionary of the whole network
        Returns:
            Nothing.
    '''
    network[subject_dwarf].remove(object_dwarf)


def is_empty_list(lst):
    '''
        Function -- is_empty_list
            Checks if the given list is an empty string.
        Parameter:
            lst -- The list to check
        Returns:
            True if the list is empty, False otherwise.
    '''
    return len(lst) == 0


def friending_validator(dwarf_to_friend, friend_lst):
    '''
        Function -- friending_validator
            Checks that a dwarf to friend exists but is not included in the
            friend list.
        Parameter:
            dwarf_to_friend -- The dwarf to friend
            friend_lst -- The friend list of the dwarf who friends someone
        Raises:
            KeyError -- If the dwarf to friend does not exist.
            ValueError -- If the dwarf to friend have been included in the
            friend list of the dwarf who is logging in.
        Returns:
            Nothing
    '''
    SEVEN_DWARVES = ("Happy", "Dopey", "Bashful", "Sneezy", "Sleepy", "Doc",
                     "Grumpy")

    if dwarf_to_friend not in SEVEN_DWARVES:
        raise KeyError
    if dwarf_to_friend in friend_lst:
        raise ValueError


def main():
    PRINT_FRIENDS = "P"
    UNFRIDEND = "U"
    FRIEND = "F"
    QUIT = "Q"

    path = "dwarves.txt"
    file_list = read_file(path)
    network = create_network(file_list)
    logging_in_dwarf = input("Which of the 7 dwarves is logging in? ")
    should_quit = False
    while not should_quit:
        print("Choose from one of the options below:")
        print("P: Print your list of friends")
        print("U <name>: Unifriend someone")
        print("F <name>: Friend someone")
        print("Q: Quit")
        user_in = input("Your choice: ")

        user_choice = user_in.split()[0]

        if user_choice == PRINT_FRIENDS:
            print("Your friends:", ", ".join(network[logging_in_dwarf]))
        elif user_choice == UNFRIDEND:
            chosen_dwarf = user_in.split()[1]
            if is_empty_list(network[logging_in_dwarf]):
                print("You don't have any friends.")
            else:
                try:
                    unfriending(logging_in_dwarf, chosen_dwarf, network)
                    unfriending(chosen_dwarf, logging_in_dwarf, network)
                    print("{} has been unfriended".format(chosen_dwarf))
                except ValueError:
                    print("{} is not your friend".format(chosen_dwarf))
        elif user_choice == FRIEND:
            chosen_dwarf = user_in.split()[1]
            try:
                friending_validator(chosen_dwarf, network[logging_in_dwarf])
                network[logging_in_dwarf].append(chosen_dwarf)
                network[chosen_dwarf].append(logging_in_dwarf)
                print("{} has been friended".format(chosen_dwarf))
            except ValueError:
                print("{} was your friend.".format(chosen_dwarf))
            except KeyError:
                print("{} doesn't exist.".format(chosen_dwarf))
        elif user_choice == QUIT:
            should_quit = True
        else:
            print("Your choice is valid.")

    content = generate_text(network)
    write_file(path, content)


if __name__ == "__main__":
    main()
