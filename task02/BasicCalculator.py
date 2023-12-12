## Calculator:

# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract num2 from num1
def subtract(num1, num2):
    return num1 - num2


# Function to divide num1 by num2
def divide(num1, num2):
    return round(num1 / num2, 2)


# Function to multiply two numbers
def multiply(num1, num2):
    return round(num1 * num2, 2)


# Flag to control the loop
response = True

# Counter to track the number of operations
count = 0

# Main loop
while (response):

    # Input for the first number
    if (count == 0):
        num1 = float(input("Enter 1st number: "))
    else:
        num1 = result  # Use the result of the previous operation as the first number

    # Input for the operation
    op = input("Enter the choice of operation (+, -, *, /): ")

    # Input for the second number
    num2 = float(input("Enter 2nd number: "))

    # Perform the selected operation
    match op:
        case "+":
            result = add(num1, num2)
        case "-":
            result = subtract(num1, num2)
        case "*":
            result = multiply(num1, num2)
        case "/":
            result = divide(num1, num2)
        case _:
            print("Invalid entry; Calculator has been reset.")
            continue

    # Display the result
    print(f"{num1} {op} {num2} = {result}")

    # Ask if the user wants to continue
    proceed = input("Press 0 to stop; any other key to continue: ")

    if (proceed == "0"):
        response = False  # Exit the loop
    else:
        count += 1  # Increment the counter for subsequent iterations

