from flask import Flask, jsonify
from flask_mysqldb import MySQL
from conexion import conn

app = Flask(__name__)

conn = MySQL(app)

if __name__ == '__main__':
    app.conexion.from_object(conn['conexion'])
    app.run(debug = True)

@app.route('/movimientos')
def movimientos():
    cur = conn.connection.cursor()
    #Consulta con los parametros para seleccionar los campos de interes
    cur.execute(

            "SELECT ida AS 'ida' , nombre AS 'nombre', edad AS 'edad' FROM alumno"

    )
    res = cur.fetchall()
    #Se recopila la informacion de la respuesta de la consulta y se agrupan los valores de los campos: tipo, anio, mes y monto, en un elemento llamado movimiento
    data = []
    for i in res:
        json = {
                    "Ida": i['ida'],
                    "Nombre": i['nombre'],
                    "Edad": i['edad']

                }
        data.append(json)
    return jsonify(data)
