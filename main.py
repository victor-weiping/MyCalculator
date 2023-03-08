import logging
from calculator import Calculator

logging.basicConfig(level='WARNING')
logger = logging.getLogger(__name__)


# use calculator compute expression, return result
def calculate(calculator, expression):
    logger.info('expression: "%s"', expression)

    # if the last char is not '=', add it
    if expression[-1] != '=':
        expression += '='

    for k in expression:
        calculator.click_button(k)
    result = calculator.get_result()

    logger.warning('calculate: %s%s', expression, result)
    return result

def main():
    # create virtual Calculator
    calculator = Calculator()

    # let calculator do the work
    while True:
        exp = input("Enter expression:")
        if exp == "":
            break
        calculate(calculator, exp)
    return

# main entry
if __name__ == '__main__':
    main()
