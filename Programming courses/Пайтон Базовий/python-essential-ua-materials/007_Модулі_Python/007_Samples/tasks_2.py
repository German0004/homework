import re
import math
import datetime

t = "I want to be a professor, but only one thing I can solve is x=exp(8)+sqrt(17)+log(5)"


def process(text):
    re_match = re.search('x=', text)
    equation = text[re_match.span()[1]:]
    ops = {'exp': math.exp, 'sqrt': math.sqrt, 'log': math.log}
    actions = equation.split('+')
    result = 0
    for action in actions:
        action = action.replace('(', ' ').replace(')', '')
        op, value = action.split(' ')
        result += ops[op](int(value))
    report = "Result = {response}; Date {date}".format(
        response=result,
        date=datetime.datetime.now().strftime('%d/%m/%y')
    )
    print(report)


process(t)
