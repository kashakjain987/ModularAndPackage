import datetime
import time
import math
import random
import string
import uuid


def datetime_menu():
    while True:
        print("\n      DATE & TIME UTILITIES")
        print("  [1] Current date and time")
        print("  [2] Difference between two dates")
        print("  [3] Format date")
        print("  [4] Stopwatch")
        print("  [5] Countdown timer")
        print("  [6] Back to main menu")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            try:
                date1 = datetime.date.fromisoformat(
                    input("Enter first date (YYYY-MM-DD): ")
                )
                date2 = datetime.date.fromisoformat(
                    input("Enter second date (YYYY-MM-DD): ")
                )
                print("Difference:", abs((date2 - date1).days), "days")

            except ValueError:
                print("Error: Please enter valid dates in YYYY-MM-DD format.")

        elif choice == "3":
            format_string = input("Enter date format (e.g. %d-%m-%Y): ")
            print(datetime.datetime.now().strftime(format_string))

        elif choice == "4":
            input("Press Enter to start.")
            start = time.time()
            input("Press Enter to stop.")
            print("Elapsed time:", round(time.time() - start, 2), "seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter countdown seconds: "))

                if seconds < 0:
                    print("Time cannot be negative.")
                    continue

                while seconds > 0:
                    print("Time remaining:", seconds)
                    time.sleep(1)
                    seconds -= 1

                print("\n*** Countdown completed! ***")

            except ValueError:
                print("Error: Please enter a whole number.")

        elif choice == "6":
            break

        else:
            print("Invalid option. Please try again.")


def math_menu():
    while True:
        print("\n     MATHEMATICAL UTILITIES")
        print("  [1] Factorial")
        print("  [2] Compound interest")
        print("  [3] Trigonometry")
        print("  [4] Area of shapes")
        print("  [5] Logarithms")
        print("  [6] Back to main menu")

        choice = input("\nSelect an option: ").strip()

        try:
            if choice == "1":
                number = int(input("Enter a non-negative integer: "))

                if number < 0:
                    print("Number cannot be negative.")
                else:
                    print("Factorial:", math.factorial(number))

            elif choice == "2":
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                years = float(input("Enter time in years: "))

                if principal < 0 or rate < 0 or years < 0:
                    print("Values cannot be negative.")
                else:
                    amount = principal * (1 + rate / 100) ** years
                    print("Final amount:", round(amount, 2))
                    print("Compound interest:", round(amount - principal, 2))

            elif choice == "3":
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                print("Sine:", round(math.sin(radians), 4))
                print("Cosine:", round(math.cos(radians), 4))
                print("Tangent:", round(math.tan(radians), 4))

            elif choice == "4":
                print("1. Circle")
                print("2. Rectangle")
                print("3. Triangle")

                shape = input("Choose a shape: ").strip()

                if shape == "1":
                    radius = float(input("Enter radius: "))

                    if radius < 0:
                        print("Radius cannot be negative.")
                    else:
                        print("Area:", round(math.pi * radius ** 2, 2))

                elif shape == "2":
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))

                    if length < 0 or width < 0:
                        print("Dimensions cannot be negative.")
                    else:
                        print("Area:", length * width)

                elif shape == "3":
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))

                    if base < 0 or height < 0:
                        print("Dimensions cannot be negative.")
                    else:
                        print("Area:", 0.5 * base * height)

                else:
                    print("Invalid option. Please try again.")

            elif choice == "5":
                number = float(input("Enter a positive number: "))

                if number <= 0:
                    print("Number must be positive.")
                else:
                    print("Natural logarithm:", round(math.log(number), 4))
                    print("Base-10 logarithm:", round(math.log10(number), 4))

            elif choice == "6":
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Error: Please enter valid numeric values.")


def random_menu():
    while True:
        print("\n       RANDOM DATA TOOLS")
        print("  [1] Random number")
        print("  [2] Random list")
        print("  [3] Password generator")
        print("  [4] OTP generator")
        print("  [5] Random sampling")
        print("  [6] Number guessing game")
        print("  [7] Back to main menu")

        choice = input("\nSelect an option: ").strip()

        try:
            if choice == "1":
                start = int(input("Enter minimum number: "))
                end = int(input("Enter maximum number: "))

                if start > end:
                    print("Minimum cannot exceed maximum.")
                else:
                    print("Random number:", random.randint(start, end))

            elif choice == "2":
                count = int(input("How many numbers? "))
                start = int(input("Enter minimum: "))
                end = int(input("Enter maximum: "))

                if count < 0 or start > end:
                    print("Error: Please check the entered values.")
                else:
                    numbers = [
                        random.randint(start, end) for _ in range(count)
                    ]
                    print("Random list:", numbers)

            elif choice == "3":
                length = int(input("Enter password length: "))

                if length < 1:
                    print("Length must be positive.")
                else:
                    characters = (
                        string.ascii_letters
                        + string.digits
                        + "!@#$%&*"
                    )

                    password = "".join(
                        random.choice(characters) for _ in range(length)
                    )

                    print("Generated password:", password)

            elif choice == "4":
                length = int(input("Enter OTP length: "))

                if length < 1:
                    print("Length must be positive.")
                else:
                    otp = "".join(random.choices(string.digits, k=length))
                    print("Generated OTP:", otp)

            elif choice == "5":
                items = [
                    item.strip()
                    for item in input(
                        "Enter items separated by commas: "
                    ).split(",")
                    if item.strip()
                ]

                count = int(input("How many items to select? "))

                if count < 0 or count > len(items):
                    print("Invalid sample size.")
                else:
                    print("Selected items:", random.sample(items, count))

            elif choice == "6":
                secret = random.randint(1, 10)
                guess = int(input("Guess a number between 1 and 10: "))

                if guess == secret:
                    print("Great! Your guess is correct.")
                else:
                    print("Incorrect. The number was", secret)

            elif choice == "7":
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Error: Please enter valid numeric values.")


def uuid_menu():
    while True:
        print("\n         UUID TOOLS")
        print("  [1] Generate UUID")
        print("  [2] Back to main menu")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            print("Your generated UUID is:", uuid.uuid4())

        elif choice == "2":
            break

        else:
            print("Invalid option. Please try again.")


def file_menu():
    while True:
        print("\n          FILE TOOLS")
        print("  [1] Create a file")
        print("  [2] Write to a file")
        print("  [3] Read a file")
        print("  [4] Append to a file")
        print("  [5] Back to main menu")

        choice = input("\nSelect an option: ").strip()

        if choice == "5":
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please choose a number from 1 to 5.")
            continue

        filename = input("Enter file name: ").strip()

        try:
            if choice == "1":
                with open(filename, "x", encoding="utf-8"):
                    pass

                print("Success: File created successfully.")

            elif choice == "2":
                content = input("Enter content: ")

                with open(filename, "w", encoding="utf-8") as file:
                    file.write(content)

                print("Success: Content saved to the file.")

            elif choice == "3":
                with open(filename, "r", encoding="utf-8") as file:
                    print("\nFile content:")
                    print(file.read())

            elif choice == "4":
                content = input("Enter content to append: ")

                with open(filename, "a", encoding="utf-8") as file:
                    file.write(content + "\n")

                print("Success: New content appended to the file.")

        except FileExistsError:
            print("Notice: This file already exists.")

        except FileNotFoundError:
            print("Error: File not found. Check the file name and try again.")

        except OSError as error:
            print("File error:", error)


def explore_module():
    modules = {
        "datetime": datetime,
        "time": time,
        "math": math,
        "random": random,
        "string": string,
        "uuid": uuid
    }

    print("\n       AVAILABLE MODULES")

    for module_name in modules:
        print(module_name)

    name = input("Enter module name to explore: ").strip()

    if name in modules:
        print("\nAttributes of", name, ":")
        print(dir(modules[name]))

    else:
        print("Error: Module not found. Choose one from the list above.")


def main():
    while True:
        print("\n     MODULE & PACKAGE TOOLKIT")
        print("          MULTI-UTILITY MENU")

        print("\nChoose a tool to get started:")
        print("  [1] Date and Time Operations")
        print("  [2] Mathematical Operations")
        print("  [3] Random Data Generation")
        print("  [4] UUID Generation")
        print("  [5] File Operations")
        print("  [6] Explore Module Attributes")
        print("  [7] Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()