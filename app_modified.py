from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    var_1 = request.form.get("var_1", type=int)
    var_2 = request.form.get("var_2", type=str)
    operation = request.form.get("operation")

    result = var_2
    if(operation == 'Only Lower char'):
        for i in range(var_1-len(var_2)):
            result += random.choice(lower)
    elif(operation == 'Lower + Upper char'):
        for i in range(var_1-len(var_2)):
            result +=  random.choice(upper)
    elif(operation == 'Lower + upper + Special char'):
        for i in range(var_1-len(var_2)):
            result += random.choice(digits)
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
