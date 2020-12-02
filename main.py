from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

to_dos = ['Comprar Cafe','Enviar Tarea','Hacer Reporte']

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

@app.route('/error500')
def error():
    return 1/0