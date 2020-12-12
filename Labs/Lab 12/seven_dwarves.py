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

     

def main():
    dwarf_name = input("Hi! Who are you?")

    print("Menu:")
    print("P - Print your list of friends")
    print("U - Unifriend someone")
    print("F - Friend someone")
    print("Q - Quit")

    path = "dwarves.txt"
    friends_lst = read_file(path)
    network = create_network(friends_lst)


