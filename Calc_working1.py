# Calculator:

#TODO 1: Create the functions

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

#TODO 2: Make the operational symbols as the Key for a Dictionary, and the Values as the function name
operations = {
    "+": add, "-": subtract, "*": multiply, "/": divide
}

num1 = float(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = float(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)
print(f"{int(num1)} {operation_symbol} {int(num2)} = {int(first_answer)}")

w = True
while w == True:

    if_only = input("Do you want to do another calculation with the last answer? (Y or N): ").upper()
    if if_only == "Y":


        for symbol in operations:
            print(symbol)

    #2nd Iteration, using Input:
    operation_symbol = input("Pick another operation: ")
    num3 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]

    second_answer = calculation_function(first_answer, num3)
    print(f"{int(first_answer)} {operation_symbol} {int(num3)} = {int(second_answer)}")

else:
    w = False



'''

w = True
while w == True:

    if_only = input("Do you want to do another calculation with the last answer? (Y or N): ").upper()
    if if_only == "Y":


        for symbol in operations:
            print(symbol)

    #2nd Iteration, using Input:
    operation_symbol = input("Pick another operation: ")
    num3 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]

    second_answer = calculation_function(first_answer, num3)
    print(f"{int(first_answer)} {operation_symbol} {int(num3)} = {int(second_answer)}")

else:
    w = False
'''

