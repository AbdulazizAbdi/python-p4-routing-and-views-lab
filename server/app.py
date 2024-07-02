#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter_string>')
def print_string(parameter_string):
    print(f'{parameter_string}')
    return f'{parameter_string}'

@app.route('/count/<int:parameter_integer>')
def count(parameter_integer):
    integer_string = ''
    for num in range(parameter_integer):
        integer_string += f'{num}\n'
    return integer_string

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        solution = num1 + num2
        return f'{solution}'
    elif operation == '-':
        solution = num1 - num2
        return f'{solution}'
    elif operation == '*':
        solution = num1 * num2
        return f'{solution}'
    elif operation == 'div':
        solution = num1 / num2
        return f'{solution}'
    elif operation == '%':
        solution = num1 % num2
        return f'{solution}'