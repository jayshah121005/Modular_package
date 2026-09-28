# Modular Package

A beginner-friendly Python **Multi-Utility Toolkit** built using separate modules and a custom utility package.

The project demonstrates how Python modules, packages, functions, file handling, date/time operations, mathematical operations, random data generation, UUIDs, and module exploration can be combined into one menu-driven application.

## Features

### 1. Datetime and Time Operations

* Display current date and time
* Calculate difference between two dates
* Format a date and time
* Stopwatch
* Countdown timer

### 2. Mathematical Operations

* Calculate factorial
* Calculate compound interest
* Trigonometric calculations
* Calculate area of geometric shapes

  * Circle
  * Rectangle
  * Triangle
* Unit conversion

  * Celsius to Fahrenheit
  * Fahrenheit to Celsius
  * Square root
  * Percentage

### 3. Random Data Generation

* Generate a random number
* Generate a random list
* Generate a random password
* Generate a random OTP

### 4. UUID Generation

* Generate a unique UUID using Python's `uuid` module

### 5. File Operations

* Create a new file
* Write data to a file
* Read data from a file
* Append data to a file

### 6. Module Exploration

* Enter a Python module name
* View its available attributes using `dir()`

## Project Structure

```text
Modular_package/
│
├── main.py
├── datetime_module.py
├── math_module.py
├── random_module.py
├── file_module.py
│
└── utils_package/
    ├── __init__.py
    └── math_utils.py
```

## Technologies Used

* Python
* Python Standard Library
* Modules
* Packages
* Functions
* Exception Handling
* File Handling
* `datetime`
* `math`
* `random`
* `uuid`

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jayshah121005/Modular_package.git
```

### 2. Open the project folder

```bash
cd Modular_package
```

### 3. Run the program

```bash
python main.py
```

## How It Works

The project uses a main menu to provide access to different modules.

```text
Multi-Utility Toolkit

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations
6. Explore Module Attributes
7. Exit
```

Each menu option calls functions from separate Python modules, making the project organized and easier to understand.

## Custom Utility Package

The project contains a custom package called `utils_package`.

The `math_utils.py` file contains utility functions for:

* Celsius to Fahrenheit conversion
* Fahrenheit to Celsius conversion
* Square root
* Percentage calculation

## Purpose

This project was created to practice:

* Python modules
* Python packages
* Importing modules
* Creating reusable functions
* Exception handling
* File handling
* Working with Python's standard library
* Building a menu-driven Python application

## Author

**Jay Shah**

GitHub:
https://github.com/jayshah121005
