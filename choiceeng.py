from scripts import *


def opt_input():  # ask for the players choice
    valid_opt = ["A", "B", "C", "D", "E", "F", "G", "H", "a", "b", "c", "d", "e", "f", "g", "h"]
    opt = str(input("Your choice: "))
    while not valid_opt.__contains__(opt):
        print("Please choose one of the options above!")
        opt = str(input("Your choice again: "))
    if opt.isupper():
        opt = opt.lower()
    return opt


def ch_error(*args):
    print("Please choose one of the options above!")
    choice(*args)


def choice(*args):
    opt = opt_input()
    match opt:
        case "a":
            try:
                eval(args[0])
            except IndexError:
                ch_error(*args)
        case "b":
            try:
                eval(args[1])
            except IndexError:
                ch_error(*args)
        case "c":
            try:
                eval(args[2])
            except IndexError:
                ch_error(*args)
        case "d":
            try:
                eval(args[3])
            except IndexError:
                ch_error(*args)
        case "e":
            try:
                eval(args[4])
            except IndexError:
                ch_error(*args)
        case "f":
            try:
                eval(args[5])
            except IndexError:
                ch_error(*args)
        case "g":
            try:
                eval(args[5])
            except IndexError:
                ch_error(*args)
        case "h":
            try:
                eval(args[6])
            except IndexError:
                ch_error(*args)

# this is an arbitrary test question with 3 options. It should evaluate your choice and if its valid, execute the code
# passed into it starting with the first option as the first passed argument!
# choice("print('option A')", "print('option B')", "print('option C')")
