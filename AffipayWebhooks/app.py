from flask import Flask, request, render_template, redirect
import mariadb
from controlador import *
from conexion import *


app = Flask(__name__)

@app.route('/webhook/<ruta>/', methods=['POST'])
def insert_json(ruta):
    ruta_usuario = existeRuta(ruta)
    if ruta_usuario != None:
        request_data = request.get_json()
        id_comercio = ruta
        bin = request_data['reference']
        lastFour = request_data['lastFour']
        mydb1 = mydb()
        conn = mydb1.cursor()
        conn.execute("INSERT INTO usuarios (id_comercio, bin, lastFour) VALUES ('%s', %s, '%s')"% (id_comercio,bin,lastFour))
        mydb1.commit()
    return 'Si existe'




@app.errorhandler(401)
def status_401(error):
    return 'error'

if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000)