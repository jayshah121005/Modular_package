import math


def factorial():
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial is not possible for negative numbers.")
        else:
            answer = math.factorial(number)
            print("Factorial:", answer)

    except ValueError:
        print("Please enter a whole number.")


def compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time_years = float(input("Enter time (in years): "))

        amount = principal * (1 + rate / 100) ** time_years
        interest = amount - principal

        print("Compound Interest:", round(interest, 2))
        print("Total Amount:", round(amount, 2))

    except ValueError:
        print("Please enter valid numbers.")


def trigonometry():
    try:
        angle = float(input("Enter angle in degrees: "))

        radians = math.radians(angle)

        sin_value = math.sin(radians)
        cos_value = math.cos(radians)
        tan_value = math.tan(radians)

        print("Sin:", round(sin_value, 4))
        print("Cos:", round(cos_value, 4))
        print("Tan:", round(tan_value, 4))

    except ValueError:
        print("Please enter a valid angle.")


def area_of_shape():
    print()
    print("Area of Geometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            radius = float(input("Enter radius: "))

            if radius < 0:
                print("Radius cannot be negative.")
                return

            area = math.pi * radius * radius

            print("Area of Circle:", round(area, 2))

        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            if length < 0 or width < 0:
                print("Length and width cannot be negative.")
                return

            area = length * width

            print("Area of Rectangle:", round(area, 2))

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base < 0 or height < 0:
                print("Base and height cannot be negative.")
                return

            area = 0.5 * base * height

            print("Area of Triangle:", round(area, 2))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")