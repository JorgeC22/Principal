from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import uuid
from controlador import ValidacionTarjetaOrigen, obtenertokenAPIinntec, obtenertokeraffipay, validacionSaldoInntec, obtenerCredenciales
from models.reportetransaccion import reportetransaccion


app = Flask(__name__)



@app.route("/")
def index():
    #flash('Mensaje de prueba!')
    return render_template('index.html')

@app.route("/cargo")
def cargo():
    #flash('Mensaje de prueba!')
    return render_template('vacio.html')

@app.route("/formulario", methods = ['POST'])
def formulario():
    reportetrans = reportetransaccion(str(uuid.uuid4()),request.form['nombre_titular'],request.form['tarjeta_origen'],request.form['cvc_origen'],request.form['monto'],request.form['tarjeta_destino'],None,None,None,request.form['email'])
    token_inntec = obtenertokenAPIinntec(reportetrans)
    if token_inntec != False:
        valTarjetaorigen = ValidacionTarjetaOrigen(reportetrans)
        if valTarjetaorigen != False:
            print(valTarjetaorigen)
            credenciales = obtenerCredenciales(valTarjetaorigen)
            print(credenciales)
            valSaldoTarjeta = validacionSaldoInntec(token_inntec,credenciales,valTarjetaorigen,reportetrans)
            return valSaldoTarjeta
        else:
            return "Num tarjeta no valida"
    else:
        return "No se obtuvo token"


if __name__== "__main__":
    #app.register_error_handler(401, status_401)
    #app.register_error_handler(404, status_404)
    app.run(debug=True)
