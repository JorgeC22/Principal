from ctypes.wintypes import INT
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import controlador


app = Flask(__name__)



@app.route("/<empresa>")
def index(empresa):
    #flash('Mensaje de prueba!')
    return render_template('index.html', data=empresa)

@app.route("/<empresa>/iniciarProceso", methods = ['POST'])
def iniciarProceso(empresa):
    idproceso = controlador.inicioProceso(request.form['nombre'],request.form['apellidoP'],request.form['apellidoM'],empresa)
    #datosP = controlador.getVariablesProceso(idproceso)
    #return render_template('pagina1.html', data=datosP)
    return "Sus datos fueron enviados correctamente."

@app.route("/pagina2", methods = ['POST'])
def pagina2():
    datosP = controlador.getVariablesProceso(request.form['idproceso'])
    return render_template('pagina2.html', data=datosP)

@app.route("/listaVerificarDatos")
def listaVerificarDatos():
    procesos = controlador.getProcesos()
    listVarP = controlador.getlistVariablesProceso(procesos)
    listP = controlador.getactividadProceso(listVarP)
    return render_template('listaVerificarDatos.html', data=listP)

@app.route("/acceso", methods = ['POST'])
def acceso():
    data = controlador.getVariablesProceso(request.form['idproceso'])
    data['verificacion'] = request.form['verificar']
    print(data)
    idtask = controlador.gettask(request.form['idproceso'])
    controlador.CompleteTask(idtask,data)
    return "Variables Aceptados"
    #return request.form['verificar']

@app.route("/acceso2", methods = ['POST'])
def acceso2():
    data = controlador.getVariablesProceso(request.form['idproceso'])
    data['verificacion'] = request.form['verificar']
    print(data)
    idtask = controlador.gettask(request.form['idproceso'])
    controlador.CompleteTask(idtask,data)
    return "Variables Rechazados"


@app.route("/taskexternall")
def taskexternall():
    hola = controlador.taskexternall()
    return "Tarea Externa Realizada"


if __name__== "__main__":
    app.run(debug=True)
