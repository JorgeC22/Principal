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


@app.route("/<comercio>")
#@login_required
def comercio():
    return render_template('home.html')

@app.route("/upload", methods = ['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['archivo']
        file.save(os.path.join(os.path.join(os.getcwd(), 'archivos'), file.filename))
        if os.path.exists('./archivos/'+file.filename):
            executor.submit(long_task, file)
            flash("Archivo subido exitosamente")
            return redirect('/home')

# Tarea que requiere mucho tiempo
def long_task(arg1):
    main(arg1)
    
@app.errorhandler(401)
def status_401(error):
    return render_template('privacidad.html'), 404

@app.errorhandler(404)
def status_404(error):
    return redirect('/')

if __name__== "__main__":
    app.run(debug=True)
