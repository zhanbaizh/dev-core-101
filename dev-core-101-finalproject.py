# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:  # Check to prevent division by zero
        return "Error! Division by zero."
    else:
        return x / y
#function to perform exponent
def power(x, y):
    return pow(x,y)

# Main calculator function
def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power(^)")

    # Get user input for the operation
    operation = input("Enter the number of the operation (1/2/3/4/5): ")

    if operation in ['1', '2', '3', '4', '5']:
        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        if operation == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")

        elif operation == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")

        elif operation == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")

        elif operation == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
        
        elif operation == '5':
            result = power(num1, num2)
            print(f"The result of {num2} power of {num1} is: {result}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()
