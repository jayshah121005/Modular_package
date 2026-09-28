def create_file():
    file_name = input("Enter file name: ")

    try:
        with open(file_name, "w") as file:
            pass

        print("File created successfully!")

    except OSError as error:
        print("Error:", error)


def write_file():
    file_name = input("Enter file name: ")
    data = input("Enter data to write: ")

    try:
        with open(file_name, "w") as file:
            file.write(data)

        print("Data written successfully!")

    except OSError as error:
        print("Error:", error)


def read_file():
    file_name = input("Enter file name: ")

    try:
        with open(file_name, "r") as file:
            data = file.read()

        print()
        print("File Content:")
        print(data)

    except FileNotFoundError:
        print("File not found.")

    except OSError as error:
        print("Error:", error)


def append_file():
    file_name = input("Enter file name: ")
    data = input("Enter data to append: ")

    try:
        with open(file_name, "a") as file:
            file.write("\n" + data)

        print("Data appended successfully!")

    except OSError as error:
        print("Error:", error)