from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
            
            
@app.route('/<cpf>')
def clonarcartao(cpf):
    cpf = int(cpf)
    lis2 = []
    lis3 = []
    for i in range(int(cpf)):
        lis = ["1","2","3","4","5","6","7","8","9"]
        string = ""

        for i in range(9):
            string = string + random.choice(lis)

        multi = 10
        lis2 = []

        for i in string:
            lis2.append(int(i) * multi)
            multi -= 1

        multi = 11

        conta = sum(lis2) % 11
        if conta >= 10:
            conta = 0

        lis2 = []

        string = string + str(conta)

        for i in string:
            lis2.append(int(i) * multi)
            multi -= 1
        
        lis2 = []

        conta = sum(lis2) % 11
        if conta >= 10:
            conta = 0

        string = string + str(conta)

        lis3.append(string)
    return jsonify({"cpfs" : lis3})

app.run(host='0.0.0.0')