from ctypes.wintypes import INT
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import controlador


app = Flask(__name__)



@app.route("/")
def index():
    #flash('Mensaje de prueba!')
    return render_template('index.html')

@app.route("/pagina1")
def pagina1():
    return render_template('pagina1.html')

@app.route("/acceso", methods = ['POST'])
def acceso():
    idproceso = controlador.inicioProceso(request.form['name'],int(request.form['age']))
    return render_template('pagina1.html', data=idproceso)


if __name__== "__main__":
    app.run(debug=True)
