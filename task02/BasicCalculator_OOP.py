# class Calculator:
#     def __init__(self, num1, num2, op):
#         self.num1 = num1
#         self.num2 = num2
#         self.op = op

class CalculatorOperator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

def selectOperation(casioCalc):

    # casio = Calculator(num1, num2, op)
    while True:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        op = input("Enter the operation you wish to perform: ")

        if op == "+":
            ans = casioCalc.add(num1, num2)
            print(f"The sum of {num1} and {num2} is {ans}.")

        elif op == "-":
            ans = casioCalc.subtract(num1, num2)
            print(f"The difference of {num1} and {num2} is {ans}.")

        elif op == "*":
            ans = casioCalc.multiply(num1, num2)
            print(f"The product of {num1} and {num2} is {ans}.")

        elif op == "/":
            ans = casioCalc.divide(num1, num2)
            print(f"The quotient of {num1} and {num2} is {ans}.")

        elif op == " ":
            print("Thank you for using calculator!")
            break

        else:
            print("Invalid Entry")

def main():
    print("Welcome to the Calculator!")
    casioCalc = CalculatorOperator()
    selectOperation(casioCalc)

if __name__ == "__main__":
    main()