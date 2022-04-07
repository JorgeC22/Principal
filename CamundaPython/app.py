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
    return render_template('variablesAceptado.html')

@app.route("/pagina2", methods = ['POST'])
def pagina2():
    datosP = controlador.getVariablesProceso(request.form['idproceso'])
    datosP = controlador.getProcesoActividad(datosP)
    return render_template('pagina2.html', data=datosP)

@app.route("/listaVerificarDatos")
def listaVerificarDatos():
    procesos = controlador.getProcesos()
    listVarP = controlador.getlistVariablesProceso(procesos)
    listP = controlador.getactividadProceso(listVarP)
    return render_template('listaVerificarDatos.html', data=listP)

@app.route("/acceso", methods = ['POST'])
def acceso():
    #data = controlador.getVariablesProceso(request.form['idproceso'])
    data = controlador.jsonParametros(
        request.form['idproceso'],
        request.form['nombre'],
        request.form['apellidoP'],
        request.form['apellidoM'],
        request.form['empresa'],
        request.form['verificar']
    )
    #data['verificacion'] = request.form['verificar']
    #print(data)
    idtask = controlador.gettask(request.form['idproceso'])
    controlador.CompleteTask(idtask,data)
    return render_template('variablesAceptado.html')

@app.route("/acceso2", methods = ['POST'])
def acceso2():
    data = controlador.jsonParametros(
        request.form['idproceso'],
        request.form['nombre'],
        request.form['apellidoP'],
        request.form['apellidoM'],
        request.form['empresa'],
        request.form['verificar']
    )
    #data = controlador.getVariablesProceso(request.form['idproceso'])
    #data['verificacion'] = request.form['verificar']
    #print(data)
    idtask = controlador.gettask(request.form['idproceso'])
    controlador.CompleteTask(idtask,data)
    return render_template('variablesAceptado.html')



if __name__== "__main__":
    app.run(debug=True)
