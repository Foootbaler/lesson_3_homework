from calculator import Calculator
from test_calculator import CalculatorTest
calc = Calculator()
calc_test = CalculatorTest()


def conversion_to_float(variable):
    try:
        float_value = float(variable)
    except ValueError:
        raise ValueError
    return float_value

while True:
    print('What kind of operation do you want to do?:\n'
          '1. Add\n'
          '2. Subtract\n'
          '3. Multiply\n'
          '4. Divide\n'
          '5. Evaluate\n'
          '0. Exit\n'
          )

    number = input()

    if number == '1':
        x = input('Input x: ')
        y = input('Input y: ')
        try:
            float_x = conversion_to_float(x)
            float_y = conversion_to_float(y)
        except ValueError:
            print('Input correct numbers')
            continue
        result = calc.add(float_x, float_y)
        print(result)
    elif number == '2':
        x = input('Input x: ')
        y = input('Input y: ')
        try:
            float_x = conversion_to_float(x)
            float_y = conversion_to_float(y)
        except ValueError:
            print('Input correct numbers')
            continue
        float_x = conversion_to_float(x)
        float_y = conversion_to_float(y)
        result = calc.subtract(float_x, float_y)
        print(result)
    elif number == '3':
        x = input('Input x: ')
        y = input('Input y: ')
        try:
            float_x = conversion_to_float(x)
            float_y = conversion_to_float(y)
        except ValueError:
            print('Input correct numbers')
            continue
        float_x = conversion_to_float(x)
        float_y = conversion_to_float(y)
        result = calc.multiply(float_x, float_y)
        print(result)
    elif number == '4':
        x = input('Input x: ')
        y = input('Input y: ')
        try:
            float_x = conversion_to_float(x)
            float_y = conversion_to_float(y)
        except ValueError:
            print('Input correct numbers')
            continue
        float_x = conversion_to_float(x)
        float_y = conversion_to_float(y)
        try:
            result = calc.divide(float_x, float_y)
        except ZeroDivisionError:
            print('ZeroDivisionError\n')
            continue
        print(result)
    elif number == '5':
        expression = input('Input expression: ')
        try:
            result = calc.evaluate(expression)
        except SyntaxError:
            print('SyntaxError\n')
            continue
        print(result)
    elif number == '0':
        break
    else:
        print('Be attentive and input correct numbers of operations!\n')
        continue

