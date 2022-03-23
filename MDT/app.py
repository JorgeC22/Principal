from flask import Flask, render_template, request, flash, redirect, session
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from concurrent.futures import ThreadPoolExecutor
from controlador import *
import os
from models.usuario import usuario

# Crear ejecutor de grupo de subprocesos
executor = ThreadPoolExecutor(2)

app = Flask(__name__)
app.secret_key = 'dont tell anyone'

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(nombre_usuario):
    return get_by_id(nombre_usuario)

@app.route("/")
def inicio():
    return render_template('login.html')

@app.route("/login", methods = ['POST'])
def login():
    usuariologin = usuario(None,request.form['nombre_usuario'],request.form['contraseña'])
    login = login_usuario(usuariologin)
    if login:
        login_user(usuariologin)
        session['usuario'] = request.form['nombre_usuario']
        return redirect('/home')
    else: 
        return redirect('/')
    return render_template('login.html')

@app.route("/home")
@login_required
def home():
    return render_template('home.html')

@app.route("/upload", methods = ['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['archivo']
        file.save(os.path.join(os.path.join(os.getcwd(), 'archivos'), file.filename))
        if os.path.exists('./archivos/'+file.filename):
            executor.submit(long_task, file)
            flash("Archivo subido exitosamente")
            return redirect('/')

# Tarea que requiere mucho tiempo
def long_task(arg1):
    main(arg1)
    
@app.errorhandler(401)
def status_401(error):
    return redirect('/')

@app.errorhandler(404)
def status_404(error):
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True)
