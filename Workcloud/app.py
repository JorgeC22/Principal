from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import controlador


app = Flask(__name__)


@app.route("/")
def index():
    #flash('Mensaje de prueba!')
    return redirect(url_for('listaVerificarDatos'))

#@app.route("/inciarProceso")
#def iniciarProceso():
#    return render_template('iniciarProceso.html')

@app.route("/startProceso")
def startProceso():
    #form_data = request.form.to_dict()
    #print(form_data)
    idproceso = controlador.inicioProceso()
    #datosP = controlador.getVariablesProceso(idproceso)
    #return render_template('pagina1.html', data=datosP)
    return redirect(url_for('listaVerificarDatos'))


#@app.route("/pagina2", methods = ['POST'])
#def pagina2():
#    datosP = controlador.getVariablesProceso(request.form['idproceso'])
#    datosP = controlador.getProcesoActividad(datosP)
#    return render_template('pagina2.html', data=datosP)


@app.route("/pagina2/<idproceso>")
def pagina2(idproceso):
    return render_template('pagina2.html')

"""
@app.route("/consultaVariables/<idproceso>", methods=['GET'])
def consultaVariables(idproceso):
    #datosP = controlador.getVariablesProceso(idproceso)
    datosP = controlador.getVariablesProceso(idproceso)
    datosP = controlador.getProcesoActividad(datosP)
    response = jsonify(datosP)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
"""


"""
@app.route("/consultaVariables/<empresa>")
def consultaVariables(empresa):
    #datosP = controlador.getVariablesProceso(idproceso)
    InstanciasProc = controlador.getProcesos()
    Proceso = controlador.extraerInstancia()
    listVarP = controlador.getlistVariablesProceso(InstanciasProc)
    Proceso = ext
    response = jsonify(datosP)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
"""

@app.route("/listaVerificarDatos")
def listaVerificarDatos():
    procesos = controlador.getProcesos()
    listVarP = controlador.getlistVariablesProceso(procesos)
    listP = controlador.getactividadProcesos(listVarP)
    return render_template('listaVerificarDatos.html', data=listP)

@app.route("/listaInstancias")
def listaInstancias():
    return render_template('listaInstancias.html')

@app.route("/consultaInstancias", methods=['GET'])
def consultaInstancias():
    procesos = controlador.getProcesos()
    listJsonP = controlador.getlistJsonProceso(procesos)
    listP = controlador.getactividadProcesos(listJsonP)
    response = jsonify(listP)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route("/enviarVariables", methods = ['POST'])
def enviarVariables():
    #data = controlador.getVariablesProceso(request.form['idproceso'])
    data = request.form.to_dict()
    #print(data)
    idtask = controlador.gettask(data['idproceso'])
    controlador.CompleteTask(idtask,data)
    return render_template('variablesAceptado.html')

@app.route("/acceso", methods = ['POST'])
def acceso():
    #data = controlador.getVariablesProceso(request.form['idproceso'])
    data = request.form.to_dict()
    #data["valDocumentacion"] = request.form['verificar']
    #print(data)
    idtask = controlador.gettask(data['idproceso'])
    controlador.CompleteTask(idtask,data)
    return render_template('variablesAceptado.html')

@app.route("/acceso2", methods = ['POST'])
def acceso2():
    data = request.form.to_dict()
    #data = controlador.getVariablesProceso(request.form['idproceso'])
    #data['verificacion'] = request.form['verificar']
    #print(data)
    idtask = controlador.gettask(request.form['idproceso'])
    controlador.CompleteTask(idtask,data)
    return render_template('variablesAceptado.html')


@app.route("/validar/<idproceso>")
def validar(idproceso):
    return render_template('enviarDocumentos.html', idproceso=idproceso)

@app.route("/consultaDatos/<idproceso>", methods=['GET'])
def consultaDatos(idproceso):
    #datosP = controlador.getVariablesProceso(idproceso)
    datosP = controlador.getJsonProceso(idproceso)
    #datosP = controlador.getProcesoActividad(datosP)
    #response = jsonify(datosP)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return datosP

@app.route("/json", methods=['POST'])
def json():
    json = request.form.listvalues()
    idproceso = request.form['idproceso']
    #print(idproceso)
    #data = controlador.datosProcesos(json)
    data = controlador.getVariableJson(idproceso)
    dataJson = controlador.datosProcesos(json,data)
    idtask = controlador.gettask(idproceso)
    controlador.CompleteTask(idtask,dataJson)
    return redirect(url_for('listaVerificarDatos'))



if __name__== "__main__":
    app.run(debug=True)
