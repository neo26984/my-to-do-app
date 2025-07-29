FILENAME = r"C:\START-HERE\Teena\python\web_app1\todos.txt"


def get_todos(filepath=FILENAME):
    """ Read a text file and return the
    list of to-do items.
    """
    with open(filepath, 'r') as file_:
        todos_ = file_.readlines()
    return todos_


def write_todos(todos_, filepath=FILENAME):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_:
        file_.writelines(todos_)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
