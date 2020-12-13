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
    WHITESPACE = " "
    return key + WHITESPACE + WHITESPACE.join(dic[key])


def generate_text(network_dic):
    text_lines = []
    for key in network_dic:
        line = generate_line(key, network_dic)
        text_lines.append(line)
    return text_lines


def write_file(path, content):
        with open(path, "w") as file:
            for line in content:
                file.write(line + "\n")

     
def unfriending(subject_name, object_name, network):
    network[subject_name].remove(object_name)


def is_empty_list(lst):
    return len(lst) == 0


def friending_validator(name, friend_lst):
    SEVEN_DWARVES = ("Happy", "Dopey", "Bashful", "Sneezy", "Sleepy", "Doc",
                     "Grumpy")

    if name in friend_lst:
        raise ValueError
    if name not in SEVEN_DWARVES:
        raise KeyError


def main():
    PRINT_FRIENDS = "P"
    UNFRIDEND = "U"
    FRIEND = "F"
    QUIT = "Q"

    path = "dwarves.txt"
    file_list = read_file(path)
    network = create_network(file_list)
    dwarf_name = input("Which of the 7 dwarves is logging in? ")
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
            print("Your friends:", ", ".join(network[dwarf_name]))
        elif user_choice == UNFRIDEND:
            chosen_name = user_in.split()[1]
            if is_empty_list(network[dwarf_name]):
                print("You don't have any friends.")
            else:
                try:
                    unfriending(dwarf_name, chosen_name, network)
                    unfriending(chosen_name, dwarf_name, network)
                    print("{} has been unfriended".format(chosen_name))
                except ValueError:
                    print("{} is not your friend".format(chosen_name))
        elif user_choice == FRIEND:
            chosen_name = user_in.split()[1]
            try:
                friending_validator(chosen_name, network[dwarf_name])
                network[dwarf_name].append(chosen_name)
                network[chosen_name].append(dwarf_name)
                print("{} has been friended".format(chosen_name))
            except ValueError:
                print("{} was your friend.".format(chosen_name))
            except KeyError:
                print("{} doesn't exist.".format(chosen_name))
        elif user_choice == QUIT:
            should_quit = True
        else:
            print("Your choice is valid.")

    content = generate_text(network)
    write_file(path, content)


if __name__ == "__main__":
    main()
