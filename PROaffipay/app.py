from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import uuid
from controlador import ValidacionTarjetaOrigen, obtenertokenAPIinntec, obtenertokeraffipay, validacionSaldoInntec
from models.reportetransaccion import reportetransaccion


app = Flask(__name__)



@app.route("/")
def inicio():
    #flash('Mensaje de prueba!')
    return render_template('inicio.html')

@app.route("/formulario", methods = ['POST'])
def formulario():
    reportetrans = reportetransaccion(str(uuid.uuid4()),request.form['nombre_titular'],request.form['tarjeta_origen'],request.form['cvv_origen'],request.form['monto'],request.form['tarjeta_destino'],None,None,None,None)
    token_inntec = obtenertokenAPIinntec()
    valTarjetaorigen = ValidacionTarjetaOrigen()
    saldoTarjetaorigen = validacionSaldoInntec(token_inntec,credenciales,idTarjeta,reportetrans)
    token_affipay_access = obtenertokeraffipay(reportetrans)
    #json = {"token": token_access}
    #flash('Mensaje de prueba!')
    return json


if __name__== "__main__":
    #app.register_error_handler(401, status_401)
    #app.register_error_handler(404, status_404)
    app.run(debug=True)
