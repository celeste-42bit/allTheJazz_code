from os import system, name

# read text files for display
def read_file(file):
    try:
        with open(file) as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print("\nThis file does not exist!\n")
        file = str(input("Goto (Filename): "))
        print(file)
        try:
            eval("read_file(file)")
        except ValueError:
            print("Error")
            exit()
        exit()  # TODO: exiting for now, make sure the error is handled in the future, so the game doesn't crash!
#    except Exception:
#        print("A fatal ERROR has occurred, while trying to read the next page!")
#        exit()  # exiting for now, make sure error is handled in the future, so the game doesn't crash!


# display text files into the console
# TODO find out how to make the whole game executable from anywhere,
# so every filepath is found no matter where it is executed from
def display(filename):
    # appended_filename = str(f"./allTheJazz_py/{filename}")  # adding the directory-path to the filename
    content = read_file(filename)  # later pass by appended_filename
    print()
    print(str(content))
    print()
    if filename[0] == "N":
        input()  # wait for user pressing enter
    elif filename[0] == "C":
        pass  # passing, because choiceeng.py will handle this
# commented out for possible removal
#    elif filename[0] == "O":
#        input()
    else:
        print("\nWaring! This file has NO PREFIX!")  # TODO: this is an error! Handle accordingly!


# create characterN.env (|N from 0 to 5 for N) from character_template.env
def character_creation():
    pass


# load character-profile from characterN.env into active_character.env
def load_active_character():
    pass


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
