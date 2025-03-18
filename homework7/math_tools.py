# filename : math_tools.py

#Math Functions scripting file

def add(a,b):
    output= a + b
    return output
    # Adds two integers

def subtract(a,b):
    output = a - b
    return output
    # Subtracts two integers

def multiply(a,b):
    output = a * b
    return output
    # Multiplies two integers

def divide(a,b):
    if b == 0:
        return(ZeroDivisionError)
        # Accounts for Dividing by Zero
    else:
        output = a / b
        return output
        # Divides Two Integers

