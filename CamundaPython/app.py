from urllib import response
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import controlador


app = Flask(__name__)


@app.route("/<empresa>")
def formulario1(empresa):
    #flash('Mensaje de prueba!')
    return render_template('index.html', data=empresa)

@app.route("/<empresa>/iniciarProceso", methods = ['POST'])
def iniciarProceso(empresa):
    form_data = request.form.to_dict()
    form_data['empresa'] = empresa
    idproceso = controlador.inicioProceso(form_data)
    #datosP = controlador.getVariablesProceso(idproceso)
    #return render_template('pagina1.html', data=datosP)
    print(form_data)
    return render_template('variablesAceptado.html')


#@app.route("/pagina2", methods = ['POST'])
#def pagina2():
#    datosP = controlador.getVariablesProceso(request.form['idproceso'])
#    datosP = controlador.getProcesoActividad(datosP)
#    return render_template('pagina2.html', data=datosP)


@app.route("/pagina2/<idproceso>")
def pagina2(idproceso):
    return render_template('pagina2.html')

@app.route("/consultaVariables/<idproceso>", methods=['GET'])
def consultaVariables(idproceso):
    #datosP = controlador.getVariablesProceso(idproceso)
    datosP = controlador.getVariablesProceso(idproceso)
    datosP = controlador.getProcesoActividad(datosP)
    response = jsonify(datosP)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

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
