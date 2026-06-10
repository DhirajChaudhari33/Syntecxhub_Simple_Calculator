def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def clear():
    print("\nCalculator Cleared!\n")


def calculator():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Clear")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "6":
            print("Thank you for using the calculator!")
            break

        elif choice == "5":
            clear()
            continue

        elif choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)
                    operator = "+"

                elif choice == "2":
                    result = subtract(num1, num2)
                    operator = "-"

                elif choice == "3":
                    result = multiply(num1, num2)
                    operator = "*"

                elif choice == "4":
                    result = divide(num1, num2)
                    operator = "/"

                print(f"\n{num1} {operator} {num2} = {result}")

            except ValueError:
                print("Error: Please enter valid numeric values.")

        else:
            print("Invalid choice! Please select a number between 1 and 6.")


# Run the calculator
calculator()