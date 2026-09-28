from datetime import datetime
import time


def show_current_datetime():
    current = datetime.now()

    print()
    print("Current Date:", current.strftime("%d-%m-%Y"))
    print("Current Time:", current.strftime("%H:%M:%S"))


def date_difference():
    first = input("Enter first date (YYYY-MM-DD): ")
    second = input("Enter second date (YYYY-MM-DD): ")

    try:
        date1 = datetime.strptime(first, "%Y-%m-%d")
        date2 = datetime.strptime(second, "%Y-%m-%d")

        difference = abs(date2 - date1)

        print("Difference:", difference.days, "days")

    except ValueError:
        print("Invalid date format.")


def format_date():
    date_input = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")

    try:
        date_value = datetime.strptime(
            date_input,
            "%Y-%m-%d %H:%M:%S"
        )

        print(
            "Formatted Date:",
            date_value.strftime("%d-%m-%Y %I:%M:%S %p")
        )

    except ValueError:
        print("Invalid date format.")


def stopwatch():
    print("Stopwatch started.")
    print("Press Enter to stop.")

    start = time.time()

    input()

    end = time.time()

    print("Time:", round(end - start, 2), "seconds")


def countdown():
    try:
        seconds = int(input("Enter seconds: "))

        for i in range(seconds, 0, -1):
            print(i)
            time.sleep(1)

        print("Time's up!")

    except ValueError:
        print("Please enter a number.")