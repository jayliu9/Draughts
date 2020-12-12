'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for making a Facebook just for the Seven Dwarves.
'''


def read_file(path):
    lines = []
    with open(file, "r") as file:
        for line in file:
            lines.append(line)
    return lines


def create_network(lines):
    network = {}
    for line in lines:
        processed_line = line_processing(line)
        network[processed_line[0]] = processed_line[1]
    return network


def line_processing(line):
    return line.strip().split(" ", 1)