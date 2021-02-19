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
    digits="0123456789 !@#$%^&*()"
    length = request.form.get("var_1", type=int)
    key = request.form.get("var_2", type=str)
    choice = request.form.get("operation")

    choices=[upper,digits]
    a=[]
    list_length=length-len(key)+1
    x=random.randint(0,list_length)

    if(choice=="Only Lower char"):
        for i in range(list_length):
            if(i==x):
                a.append(key)
            else:
                a.append(random.choice(lower))
    
    elif(choice=="Lower + Upper char"):
        for i in range(list_length):
            if(i==x):
                a.append(key)
            else:
                a.append(random.choice(upper))
    
    elif(choice=="Lower + upper + Special char"):
        for i in range(list_length):
            if(i==x):
                a.append(key)
            else:
                y=random.randint(0,1)
                c=choices[y]
                a.append(random.choice(c))
    
    str1=""
    password=str1.join(a)
    entry=password
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
