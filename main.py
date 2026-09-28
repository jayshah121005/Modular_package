import datetime_module
import math_module
import random_module
import file_module
import uuid

from utils_package.math_utils import celsius_to_fahrenheit
from utils_package.math_utils import fahrenheit_to_celsius
from utils_package.math_utils import square_root
from utils_package.math_utils import percentage


def datetime_menu():

    while True:

        print()
        print("Datetime and Time Operations:")
        print("-" * 35)
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_module.show_current_datetime()

        elif choice == "2":
            datetime_module.date_difference()

        elif choice == "3":
            datetime_module.format_date()

        elif choice == "4":
            datetime_module.stopwatch()

        elif choice == "5":
            datetime_module.countdown()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def math_menu():

    while True:

        print()
        print("Mathematical Operations:")
        print("-" * 30)
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Unit Conversion")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            math_module.factorial()

        elif choice == "2":
            math_module.compound_interest()

        elif choice == "3":
            math_module.trigonometry()

        elif choice == "4":
            math_module.area_of_shape()

        elif choice == "5":
            unit_conversion()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def unit_conversion():

    while True:

        print()
        print("Unit Conversion:")
        print("-" * 25)
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Square Root")
        print("4. Percentage")
        print("5. Back")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                celsius = float(input("Enter temperature in Celsius: "))

                answer = celsius_to_fahrenheit(celsius)

                print("Fahrenheit:", round(answer, 2))

            elif choice == "2":

                fahrenheit = float(
                    input("Enter temperature in Fahrenheit: ")
                )

                answer = fahrenheit_to_celsius(fahrenheit)

                print("Celsius:", round(answer, 2))

            elif choice == "3":

                number = float(input("Enter number: "))

                answer = square_root(number)

                if isinstance(answer, str):
                    print(answer)
                else:
                    print("Square Root:", round(answer, 2))

            elif choice == "4":

                value = float(input("Enter value: "))
                total = float(input("Enter total: "))

                answer = percentage(value, total)

                if isinstance(answer, str):
                    print(answer)
                else:
                    print("Percentage:", round(answer, 2), "%")

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid numbers.")


def random_menu():

    while True:

        print()
        print("Random Data Generation:")
        print("-" * 30)
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            random_module.random_number()

        elif choice == "2":
            random_module.random_list()

        elif choice == "3":
            random_module.random_password()

        elif choice == "4":
            random_module.random_otp()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def generate_uuid():

    print()
    print("Generate Unique Identifiers (UUID)")
    print("-" * 40)

    new_uuid = uuid.uuid4()

    print("Generated UUID:", new_uuid)


def file_menu():

    while True:

        print()
        print("File Operations:")
        print("-" * 25)
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_module.create_file()

        elif choice == "2":
            file_module.write_file()

        elif choice == "3":
            file_module.read_file()

        elif choice == "4":
            file_module.append_file()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def explore_module():

    module_name = input("Enter module name to explore: ")

    try:

        module = __import__(module_name)

        print()
        print("Available Attributes in", module_name, ":")
        print("-" * 50)

        attributes = dir(module)

        print(attributes)

    except ModuleNotFoundError:
        print("Module not found.")

    except Exception as error:
        print("Error:", error)


def main():

    while True:

        print()
        print("=" * 50)
        print("Welcome to Multi-Utility Toolkit")
        print("=" * 50)

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print()
            print("Thank you for using the Multi-Utility Toolkit!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()