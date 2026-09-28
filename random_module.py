import random
import string


def random_number():
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Starting number cannot be greater than ending number.")
            return

        number = random.randint(start, end)

        print("Random Number:", number)

    except ValueError:
        print("Please enter valid numbers.")


def random_list():
    try:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))
        size = int(input("Enter how many numbers: "))

        if start > end:
            print("Starting number cannot be greater than ending number.")
            return

        if size <= 0:
            print("List size must be greater than 0.")
            return

        numbers = []

        for i in range(size):
            number = random.randint(start, end)
            numbers.append(number)

        print("Random List:", numbers)

    except ValueError:
        print("Please enter valid numbers.")


def random_password():
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than 0.")
            return

        characters = (
            string.ascii_letters
            + string.digits
            + "!@#$%&*"
        )

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid length.")


def random_otp():
    otp = random.randint(100000, 999999)

    print("Generated OTP:", otp)