def read_file(file):
    try:
        with open(file) as f:
            content = f.read()
            f.close()
            return content
    except FileNotFoundError:
        print("\nThis file does not exist!")
        exit()  # TODO: exiting for now, make sure error is handled in the future, so the game doesn't crash!
    except:
        print("A fatal ERROR has occurred, while trying to read the next page!")
        exit()  # exiting for now, make sure error is handled in the future, so the game doesn't crash!


def display(filename):
    content = read_file(filename)
    print()
    print(str(content))
    print()
    if filename[0] == "N":
        input()  # essentially wait for user pressing enter
    elif filename[0] == "C":
        pass  # passing, because choiceeng.py will handle this
    elif filename[0] == "O":
        input()
    else:
        print("\nWaring! This file has NO PREFIX!")  # TODO: this is an error! Handle accordingly!
