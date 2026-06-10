# Simple Calculator

A simple command-line calculator built using Python. This project performs basic arithmetic operations such as addition, subtraction, multiplication, and division through a menu-driven interface.

## Features

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Clear screen option
* Input validation
* Division-by-zero handling
* User-friendly menu system
* Modular functions for better code organization and testing

## Technologies Used

* Python 3

## Project Structure

```text
Syntecxhub_Simple_Calculator/
│
├── cal.py
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/DhirajChaudhari33/Syntecxhub_Simple_Calculator.git
```

2. Navigate to the project directory:

```bash
cd Syntecxhub_Simple_Calculator
```

3. Run the program:

```bash
python cal.py
```

## Sample Output

```text
===== SIMPLE CALCULATOR =====
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Clear
6. Exit

Enter your choice (1-6): 1
Enter first number: 10
Enter second number: 5

10.0 + 5.0 = 15.0
```

## Functions

| Function       | Description                                         |
| -------------- | --------------------------------------------------- |
| add(a, b)      | Returns the sum of two numbers                      |
| subtract(a, b) | Returns the difference of two numbers               |
| multiply(a, b) | Returns the product of two numbers                  |
| divide(a, b)   | Performs division and handles divide-by-zero errors |
| clear()        | Clears the calculator session message               |
| calculator()   | Main function that controls the menu-driven program |

## Error Handling

* Prevents division by zero.
* Handles invalid numeric inputs using exception handling.
* Validates menu selections.

## Learning Outcomes

Through this project, I learned:

* Python functions
* Conditional statements
* Loops
* Exception handling
* User input processing
* Modular programming

## Author

**Dhiraj Chaudhari**

GitHub: https://github.com/DhirajChaudhari33

## License

This project is created for educational and learning purposes.
