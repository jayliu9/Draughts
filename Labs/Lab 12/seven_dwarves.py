'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for making a Facebook just for the Seven Dwarves.
'''


def read_file(path):
    lines = []
    try:
        with open(path, "r") as file:
            for line in file:
                lines.append(line)
    except FileNotFoundError:
        print("File not found")
    return lines


def create_network(lines):
    network = {}
    for line in lines:
        processed_line = line_processing(line)
        network[processed_line[0]] = processed_line[1:]
    return network


def line_processing(line):
    return line.strip().split(" ")


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


def main():
    PRINT_FRIENDS = "P"
    UNFRIDEND = "U"
    FRIEND = "F"
    QUIT = "Q"

    path = "dwarves.txt"
    file_list = read_file(path)
    network = create_network(file_list)
    dwarf_name = input("Which of the 7 dwarves is logging in?")

    print("Choose from one of the options below:")
    print("P: Print your list of friends")
    print("U <name>: Unifriend someone")
    print("F <name>: Friend someone")
    print("Q: Quit")
    user_in = input("Your choice: ")

    user_choice = user_in.split()[0]

    if user_choice == PRINT_FRIENDS:
        print("Your friends: ", ",".join(network[dwarf_name]))
    elif user_choice == UNFRIDEND:
        chosen_name = user_in.split()[1]
        try:
            unfriending(dwarf_name, chosen_name, network)
            unfriending(chosen_name, dwarf_name, network)
        except ValueError:
            print("{} is not your friend".format(chosen_name))
        
    
        


