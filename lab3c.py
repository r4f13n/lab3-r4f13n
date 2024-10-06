#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: 101775229

def operate(number1, number2, operator):
    if operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    elif operator == 'multiply':
        result = number1 * number2
    else:
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add'))        # Expected output: 15
    print(operate(10, 5, 'subtract'))   # Expected output: 5
    print(operate(10, 5, 'multiply'))   # Expected output: 50
    print(operate(10, 5, 'divide'))     # Expected output: Error message

