from conexion import conect
import json


def mostrar(emp):
    conexxion = conect()
    jpel = []
    with conexxion.cursor() as cursor:
        cursor.execute("SELECT * FROM peliculas WHERE emp = '%s'" % emp )
        peliculas = cursor.fetchall()
        for resp in peliculas:
            arc = {
                "id": resp[0],
                "titulo": resp[1],
                "anio": resp[2]
            }
            jpel.append(arc)

    #return json.dumps(jpel
    return jpel


def login_user(correo, password):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        cursor.execute("SELECT * FROM user")
        userdata = cursor.fetchall()
        for x in userdata:
            if x[1] == correo and x[2] == password:
                permiso = { "acceso": "true", "empresa": x[3] }
                break
            else:
                permiso = { "acceso": "false", "empresa": None }
        return permiso
