from flask import Flask, request
from fractions import Fraction
import statistics

app = Flask(__name__)


def in_take():
    if request.method != 'GET':
        x = request.values.get('X', default=0, type=str)
    else:
        x = request.args.get('X', default=0, type=str)
    try:
        new_values = []
        for val in x.split(','):
            new_values.append(Fraction(val))
    except ValueError:
        warning = "Enter a valid input vector. "
        return warning
    return new_values


@app.route('/median', methods=['GET', 'POST'])
def median():
    try:
        list = in_take()
        result = statistics.median(list)
    except ValueError:
        warning = in_take()
        return warning
    else:
        if float(result).is_integer():
            result = int(result)
            return "%d \n" % result
        else:

            return str(float(round(result, 4))) + " \n"


if __name__ == "__main__":
    app.run(debug=False)
