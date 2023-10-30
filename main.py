from art import logo
import math

# Function to add two numbers
def Add(n1, n2):
    return n1 + n2

# Function to subtract two numbers
def Subtract(n1, n2):
    return n1 - n2

# Function to divide two numbers (handles division by zero)
def Divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero"

# Function to multiply two numbers
def Multiply(n1, n2):
    return n1 * n2

# Function to calculate the modulus of two numbers (handles division by zero)
def Modulus(n1, n2):
    if n2 != 0:
        return n1 % n2
    else:
        return "Cannot calculate modulus with zero divisor"

# Function to calculate the square root of a number (handles negative input)
def SquareRoot(n):
    if n >= 0:
        return math.sqrt(n)
    else:
        return "Cannot calculate square root of a negative number"

# Function to square a number
def Square(n):
    return n ** 2

# Dictionary of operators and their corresponding functions
operators = {
    "+": Add,
    "-": Subtract,
    "*": Multiply,
    "/": Divide,
    "%": Modulus,
    "sqrt": SquareRoot,
    "square": Square,
}

# Main calculator function
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operators:
        print(operator)
    should_continue = True

    while should_continue:
        operator_symbol = input("Pick an operation: ")
        if operator_symbol not in operators:
            print("Invalid operator. Please choose a valid operator.")
            continue
        if operator_symbol == "sqrt" or operator_symbol == "square":
            result = operators[operator_symbol](num1)
            print(f"{operator_symbol}({num1}) = {result}")
        else:
            num2 = float(input("What's the next number?: "))
            calculation_function = operators[operator_symbol]
            result = calculation_function(num1, num2)
            print(f"{num1} {operator_symbol} {num2} = {result}")

        user_choice = input(f"Type 'y' to continue with {result}, 'n' to start a new calculation, or 'e' to exit: ")
        if user_choice == "n":
            should_continue = False
        elif user_choice == "e":
            return
        else:
            num1 = result

# Start the calculator
calculator()
