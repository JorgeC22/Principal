from ctypes.wintypes import INT
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import controlador


app = Flask(__name__)



@app.route("/")
def index():
    #flash('Mensaje de prueba!')
    return render_template('index.html')

@app.route("/pagina1", methods = ['POST'])
def pagina1():
    idproceso = controlador.inicioProceso(request.form['nombre'],request.form['apellidoP'],request.form['apellidoM'])
    datosP = controlador.getVariablesProceso(idproceso)
    return render_template('pagina1.html', data=datosP)

@app.route("/pagina2", methods = ['POST'])
def pagina2():
    datosP = controlador.getVariablesProceso(request.form['idproceso'])
    return render_template('pagina2.html', data=datosP)

@app.route("/acceso", methods = ['POST'])
def acceso():
    #data = controlador.getVariablesProceso(request.form['idproceso'])
    #data['verificacion'] = request.form['verificar']
    #print(data)
    #idtask = controlador.gettask(request.form['idproceso'])
    #controlador.CompleteTask(idtask,data)
    #return "Proceso Humano Completado"
    return request.form['verificar']

@app.route("/acceso2", methods = ['POST'])
def acceso2():
    return request.form['verificar']


if __name__== "__main__":
    app.run(debug=True)
