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
        result = num1 / num2
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

