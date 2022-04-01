from conexion import *

def existeRuta(ruta):
    mydb1 = mydb()
    with mydb1.cursor(dictionary = True) as cursor:
        cursor.execute("""SELECT url FROM url_webhook WHERE url ='""" + ruta + """' limit 1""")
        ruta_usuarios = cursor.fetchone()
    return ruta_usuarios