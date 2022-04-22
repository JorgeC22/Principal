from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import controlador


app = Flask(__name__)


@app.route("/")
def index():
    #flash('Mensaje de prueba!')
    return render_template('index.html')

@app.route("/registro")
def registro():
    return render_template('cargaDocumentos.html')

@app.route("/registro", methods=['POST'])
def cargaDocumentos():
    form_documentos = request.form.to_dict()
    idproceso = controlador.inicioProceso(form_documentos)
    return "Se cargaron los documentos."


@app.route("/listaInstancias", methods=['POST'])
def listaInstancias():
    form_data = request.form.to_dict()
    print(form_data)
    #flash('Mensaje de prueba!')
    return redirect(url_for('index'))

@app.route("/proceso/<idproceso>", methods=['POST'])
def proceso(idproceso):
    form_data = request.form.to_dict()
    print(form_data)
    #flash('Mensaje de prueba!')
    return redirect(url_for('index'))


@app.route("/crearContrato", methods=['POST'])
def crearContrato():
    form_data = request.form.to_dict()
    print(form_data)
    #flash('Mensaje de prueba!')
    return redirect(url_for('index'))


@app.route("/cargaContrato", methods=['POST'])
def cargaContrato():
    form_data = request.form.to_dict()
    print(form_data)
    #flash('Mensaje de prueba!')
    return redirect(url_for('index'))

if __name__== "__main__":
    app.run(debug=True)
