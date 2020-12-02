from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

to_dos = ['Comprar Cafe','Enviar Tarea','Hacer Reporte']

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)
    
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'to_dos':to_dos,
    }

    return render_template('hello.html', **context)

