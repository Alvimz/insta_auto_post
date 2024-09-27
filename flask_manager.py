from flask import Flask, render_template, request
import os
from json_import import JsonImport

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('base.html')

@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = request.form['senha']
    nome_arquivo = request.form['nome_arquivo']
    json_import = JsonImport()
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'a') as file:
            json_import.add_account(login,senha)
    json_import.add_account(login, senha)
    json_import.save_json(nome_arquivo)
    
    return f"Conta adicionada ao JSON: {nome_arquivo}"
