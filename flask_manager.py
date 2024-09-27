from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def principal():
     return render_template('base.html')


@app.route('/login',methods=['POST'])
def login():
    login = request.form['login']
    password = request.form['senha']
    
    