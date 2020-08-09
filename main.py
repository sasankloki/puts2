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
        new_values=[]
        for val in x.split(','):
            new_values.append(Fraction(val))
        
       
    except ValueError:
        warning = "Enter a valid input vector. "
        return warning


    return new_values



@app.route('/mean', methods=['GET', 'POST'])
@app.route('/average', methods=['GET', 'POST'])
@app.route('/avg', methods=['GET', 'POST'])
def mean():
    try:
        new_values = in_take()
        result =statistics.mean(new_values) 
    except ValueError:
        warning = in_take()
        return warning
    else:
        if float(result).is_integer():
            answer = int(result)
            return "%d \n" % answer
        else:
            
            return str(float(round(result, 3))) + " \n"



if __name__=="__main__":
    app.run(debug=True)

