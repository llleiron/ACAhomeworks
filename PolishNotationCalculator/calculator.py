import os
from datetime import datetime

def calculate(oper: str, num1: float, num2:float):
    if oper == '+' or oper == 'add':
        result = num1 + num2
    elif oper == '-' or oper == 'sub':
        result = num1 - num2
    elif oper == '*' or oper == 'mul':
        result = num1 * num2
    elif oper == '/' or oper == 'div':
        result = num1 / nimport os
from datetime import datetime


def calculate(oper: str, num1: float, num2: float):
    if oper == '+' or oper == 'add':
        result = num1 + num2
    elif oper == '-' or oper == 'sub':
        result = num1 - num2
    elif oper == '*' or oper == 'mul':
        result = num1 * num2
    elif oper == '/' or oper == 'div':
        result = num1 / num2
    return result


ExceptionMessage = 'Invalid expression'
abs_path = os.getcwd()

while True:
    expression = input('Expression: ').split()
    if (expression[0] == '+' or expression[0] == 'add' or expression[0] == '-' or expression[0] == 'sub' or expression[0] == '*' or expression[0] == 'mul' or expression[0] == '/' or expression[0] == 'div') and expression[1].isdigit() and expression[2].isdigit() and len(expression) == 3:
        result = calculate(str(expression[0]), float(
            expression[1]), float(expression[2]))
        with open(os.path.join(abs_path, 'logging', 'summary.txt'), 'a') as txt_file:
            txt_file.write(f'{datetime.now()}' + ' :: ' + 'INFO' + ' :: ' +
                           f'{expression[0]}' + ' ' + f'{expression[1]}' + ' ' + f'{expression[2]}' + ' :: ' + f'{result}' + '\n')
        with open(os.path.join(abs_path, 'logging', 'summary.txt'), 'r') as txt_file:
            data = txt_file.read()
            Errorcount = data.count("ERROR")
            Infocount = data.count("INFO")
        print('Result: ', result, '\n',
              f'Report: INFO-{Infocount}, ERROR-{Errorcount}\n', sep='')
    else:
        with open(os.path.join(abs_path, 'logging', 'summary.txt'), 'a') as txt_file:
            txt_file.write(f'{datetime.now()}' + ' :: ' +
                           'ERROR' + ' :: ' + f'{ExceptionMessage}' + ' :: ')
            for i in expression:
                txt_file.write(i + ' ')
            txt_file.write('\n')
        with open(os.path.join(abs_path, 'logging', 'summary.txt'), 'r') as txt_file:
            data = txt_file.read()
            Errorcount = data.count("ERROR")
            Infocount = data.count("INFO")
        print(f'ERROR: {ExceptionMessage}', '\n',
              f'Report: INFO-{Infocount}, ERROR-{Errorcount}\n', sep='')
um2
    return result

Errorcount: int = 0
Infocount: int = 0
ExceptionMessage = 'Invalid expression'
abs_path = os.getcwd()
while True:
    operation, inputnumber1, inputnumber2 = input('Expression: ').split()
    if (operation == '+' or operation == 'add' or operation == '-' or operation == 'sub' or operation == '*' or operation == 'mul' or operation == '/' or operation == 'div') and inputnumber1.isdigit() and inputnumber2.isdigit():
        Infocount += 1
        result = calculate(str(operation), float(inputnumber1), float(inputnumber2))
        print('Result: ', result, '\n', f'Report: INFO-{Infocount}, ERROR-{Errorcount}\n',sep='')
        with open(os.path.join(abs_path, 'logging', 'summary.txt'), 'a') as txt_file:
            txt_file.write(f'{datetime.now()}' + ' :: ' + 'INFO' + ' :: ' + f'{operation}' + ' ' + f'{inputnumber1}' + ' ' + f'{inputnumber2}' + ' :: ' + f'{result}' + '\n')
    else:
        Errorcount += 1
        print(f'ERROR: {ExceptionMessage}', '\n', f'Report: INFO-{Infocount}, ERROR-{Errorcount}\n',sep='')
        with open(os.path.join(abs_path, 'logging', 'summary.txt'), 'a') as txt_file:
            txt_file.write(f'{datetime.now()}' + ' :: ' + 'ERROR' + ' :: ' + f'{ExceptionMessage}' + ' :: ' + f'{operation}' + ' ' + f'{inputnumber1}' + ' ' + f'{inputnumber2}' + '\n')

