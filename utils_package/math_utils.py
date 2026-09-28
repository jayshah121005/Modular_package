import math


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def square_root(number):
    if number < 0:
        return "Cannot calculate square root of a negative number."

    return math.sqrt(number)


def percentage(value, total):
    if total == 0:
        return "Cannot divide by zero."

    return (value / total) * 100