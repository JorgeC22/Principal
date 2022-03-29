from flask import Flask, render_template, request, flash, redirect
from concurrent.futures import ThreadPoolExecutor
from controlador import main
import os

# Crear ejecutor de grupo de subprocesos
executor = ThreadPoolExecutor(2)

app = Flask(__name__)
app.secret_key = 'dont tell anyone'

@app.route("/")
def inicio():
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
    app.run(host='0.0.0.0', port=5000)
