# Module & Package Toolkit

## Overview

The **Module & Package Toolkit** is a menu-driven Python program that
brings together several useful utilities in one place. It uses Python's
built-in modules to perform date and time operations, mathematical
calculations, random data generation, UUID generation, file handling,
and module exploration.

## Features

### 1. Date and Time Operations

-   Display the current date and time.
-   Calculate the difference between two dates.
-   Format the current date using a custom format.
-   Measure elapsed time with a stopwatch.
-   Run a countdown timer.

### 2. Mathematical Operations

-   Calculate the factorial of a non-negative integer.
-   Calculate compound interest.
-   Calculate sine, cosine, and tangent for an angle in degrees.
-   Calculate the area of a circle, rectangle, or triangle.
-   Calculate natural and base-10 logarithms.

### 3. Random Data Generation

-   Generate a random integer within a chosen range.
-   Generate a list of random integers.
-   Generate a random password.
-   Generate a numeric OTP.
-   Select a random sample from a list of items.
-   Play a number-guessing game.

### 4. UUID Generation

-   Generate a UUID.
-   Return to the main menu without closing the program.

### 5. File Operations

-   Create a new file.
-   Write content to a file.
-   Read and display file contents.
-   Append content to a file.

### 6. Module Attribute Explorer

-   Explore attributes of the built-in `datetime`, `time`, `math`,
    `random`, `string`, and `uuid` modules.

## Requirements

-   Python 3.x
-   No external packages are required; the program uses Python's
    standard library.

## How to Run

1.  Save the program as `ModularAndPackage.py`.

2.  Open a terminal or command prompt in the folder containing the file.

3.  Run:

    ``` bash
    python multi_utility_toolkit_fixed.py
    ```

    On some systems, you may need to use `python3` instead of `python`.

4.  Choose an option from the main menu by entering its number.

5.  Follow the on-screen instructions.

6.  Use each submenu's **Back to main menu** option to return to the
    main menu. Select **7** in the main menu to exit.

## Project Structure

``` text
Module-Package-Toolkit/
├── multi_utility_toolkit_fixed.py
└── README.md
```

## Error Handling

-   Invalid menu selections display an error message.
-   Invalid numeric input is handled where numeric values are requested.
-   Date input is checked against the `YYYY-MM-DD` format.
-   File operations handle common file errors, including missing files
    and files that already exist.

## Notes

-   File operations use the current working directory unless a different
    path is entered.
-   The file creation option does not overwrite an existing file.
-   The write option replaces the existing file's contents.
-   The append option adds content at the end of the file.
-   This is a beginner-friendly project for practising Python functions,
    loops, conditionals, exception handling, imports, and file handling.


