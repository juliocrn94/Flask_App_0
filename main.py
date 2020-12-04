from flask import Flask, request, make_response, redirect, render_template, session,url_for,flash

from flask_bootstrap import Bootstrap

import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

to_dos = ['Comprar Cafe','Enviar Tarea','Hacer Reporte']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def inter_serv(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip']=user_ip
    
    return response

@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')

    context = {
        'user_ip':user_ip,
        'to_dos':to_dos,
        'username':username
    }
    
    return render_template('hello.html', **context)

@app.route('/error500')
def error():
    return 1/0