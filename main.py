from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)


def in_take():
    if request.method != 'GET':
        x = request.values.get('X', default=0, type=str) 

    else:
        
        x = request.args.get('X', default=0, type=str)
    try:
        new_values=[]
        for val in x.split(','):
            new_values.append(Fraction(val))
        
       
    except ValueError:
        warning = "Enter a valid input vector. "
        return warning

    return new_values


if __name__=="__main__":
    app.run(debug=True)

