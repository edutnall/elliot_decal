#calc is short for calculator chat

# File Name: calculator.py

# Scripting for Calculator

import math_tools as mt

while True:
    import math_tools as mt
    num1 = input('Choose your first number:')
    file = open("/Users/mapse/python_decal/elliot_decal/homework7/calc_history.txt", "a")
    if num1 == 'q':
        print("Goodbye!")
        file.close()
        break
    elif num1.isdigit() == True:
        num1 = int(num1)
        num2 = input('Choose your second number:')
        if num2.isdigit() == True:
            num2 = int(num2)
            operator = input('Choose your operation: +, -, *, / ')
            if operator == '+':
                output = mt.add(int(num1), int(num2))
                print(output)
                file.write(f'{num1} {operator} {num2} = {output}' + '\n')
            if operator == '-':
                output = mt.subtract(int(num1), int(num2))
                print(output)
                file.write(f'{num1} {operator} {num2} = {output}' + '\n')
            if operator == '*':
                output = mt.multiply(int(num1), int(num2))
                print(output)
                file.write(f'{num1} {operator} {num2} = {output}' + '\n')
            if operator == '/':
                output = mt.divide(int(num1), int(num2))
                print(output)
                file.write(f'{num1} {operator} {num2} = {output}' + '\n')
        else:
            print(TypeError, type(num2), 'Type must be integer')
    else:
        print(TypeError, type(num1), 'Type must be integer')


