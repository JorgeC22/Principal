from re import X
from sqlalchemy import sql
from conexion import conect
import json
import bcrypt
from models.user import User


def mostrar():
    conexxion = conect()
    jpel = []
    with conexxion.cursor() as cursor:
        cursor.execute("SELECT * FROM user" )
        peliculas = cursor.fetchall()
        for resp in peliculas:
            arc = {
                "id": resp[0],
                "username": resp[1],
                "password": resp[2],
                "distribuidor": resp[3],
                "grupo_trabajo": resp[4]
            }
            jpel.append(arc)

    #return json.dumps(jpel)
    return jpel


def loggin_user(correo, password):
    password = password.encode("utf-8")
    conexxion = conect()
    with conexxion.cursor() as cursor:
        cursor.execute("""select user.iduser, username, password, distribuidor, grupo_trabajo 
                            from user inner join user_distribuidor_grupotrabajo 
                            where user.iduser = user_distribuidor_grupotrabajo.iduser""")
        userdata = cursor.fetchall()
        for x in userdata:
            pass_BD = x[2].encode("utf-8")
            if x[1] == correo and bcrypt.checkpw(password, pass_BD):
                #permiso = { "acceso": "true", "empresa": x[3] }
                user = User(x[0],x[1],x[2], x[3], x[4])
                break
            else:
                #permiso = { "acceso": "false", "empresa": None }
                user = None
    return user

def loader_user(id):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        cursor.execute("""select user.iduser, username, distribuidor, grupo_trabajo 
                            from user inner join user_distribuidor_grupotrabajo 
                            where user.iduser = user_distribuidor_grupotrabajo.iduser and user.iduser = '%s'""" % id)
        userdata = cursor.fetchall()
        for x in userdata:
            if userdata != None:
                user = User(x[0],x[1],None,x[2],x[3])
                break
            else:
                user = None
        
        return user



def insertar_usuario(username,password,distribuidor,grupotrabajo):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        try:
            insert_user = "insert into usuarios values(123455,'"+username+"','"+password+"')"
            insert_user_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo values(123455,'%s','%s')" % (distribuidor,grupotrabajo)
            sqls = [insert_user, insert_user_distribuidor_gt]
            for c in sqls:
                cursor.execute(c)
            conexxion.commit()
            insert = True
        except:
            insert = False
        
    return insert


def obtener_usuarios():
    conexxion = conect()
    usuarios = []
    with conexxion.cursor() as cursor:
        cursor.execute("""select usuarios.iduser, username, distribuidor, grupo_trabajo 
                            from usuarios inner join usuario_distribuidor_grupotrabajo 
                            where usuarios.iduser = usuario_distribuidor_grupotrabajo.iduser""")
        usuarios = cursor.fetchall()
    conexxion.close()
    return usuarios

def eliminar_usuario(iduser):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        delete_user = "delete from usuarios where iduser = "+iduser+""
        delete_user_distribuidor_grupotrabajo = "delete from usuario_distribuidor_grupotrabajo where iduser = "+iduser+""
        sqls = [delete_user_distribuidor_grupotrabajo,delete_user]
        for c in sqls:
            cursor.execute(c)
        conexxion.commit()
    delete = True
    return delete

def actualizar_usuario_consulta(iduser):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        cursor.execute("select usuarios.iduser, username, distribuidor, grupo_trabajo from usuarios inner join usuario_distribuidor_grupotrabajo where usuarios.iduser = usuario_distribuidor_grupotrabajo.iduser and usuarios.iduser = "+iduser+"")
        userdata = cursor.fetchall()
        
        return userdata


"""def login_user(correo, password):
    password = password.encode("utf-8")
    conexxion = conect()
    with conexxion.cursor() as cursor:
        cursor.execute("SELECT * FROM user")
        userdata = cursor.fetchall()
        for x in userdata:
            pass_BD = x[2].encode("utf-8")
            if x[1] == correo and bcrypt.checkpw(password, pass_BD):
                permiso = { "acceso": "true", "empresa": x[3] }
                break
            else:
                permiso = { "acceso": "false", "empresa": None }
        return permiso
"""

"""def login_user(correo, password):
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
        return permiso"""
