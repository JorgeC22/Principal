import imp
from re import X
from turtle import update
from sqlalchemy import sql
from conexion import conect
import json
import bcrypt
from models.user import User
import hashlib


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
    passencode = password.encode("utf-8")
    pass_seg_encode = bcrypt.hashpw(passencode, bcrypt.gensalt())
    pass_segura = pass_seg_encode.decode()


 
    conexxion = conect()
    with conexxion.cursor() as cursor:
        try:
            sqls = []
            insert_user = "insert into usuarios values(123455,'"+username+"','"+pass_segura+"')"
            sqls.append(insert_user)
            if grupotrabajo:
                for r in grupotrabajo:
                    insert_user_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo values(123455,'%s','%s')" % (distribuidor,r)
                    sqls.append(insert_user_distribuidor_gt)
            else:
                insert_user_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo values(123455,'%s','')" % (distribuidor)
                sqls.append(insert_user_distribuidor_gt)
            for c in sqls:
                cursor.execute(c)
            conexxion.commit()
            insert = True
        except:
            insert = False
        
    return insert


def obtener_usuarios():
    conexxion = conect()
    data = []
    with conexxion.cursor() as cursor:
        cursor.execute("""select usuarios.iduser, username, distribuidor, grupo_trabajo 
                            from usuarios inner join usuario_distribuidor_grupotrabajo 
                            where usuarios.iduser = usuario_distribuidor_grupotrabajo.iduser""")
        usuarios = cursor.fetchall()
        for i in usuarios:
            if(i[3]==None):
                gtrabajo = " " 
            else:
                gtrabajo = i[3]

            idencode = str(i[0]).encode()
            hashID = hashlib.new("sha1",idencode)
            json = {
                        "id": hashID.hexdigest(),
                        "username": i[1],
                        "distribuidor": i[2],
                        "grupotrabajo": gtrabajo
                    }
            data.append(json)
    return data

def eliminar_usuario(iduser):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        delete_user = "delete from usuarios where iduser = "+str(iduser)+""
        delete_user_distribuidor_grupotrabajo = "delete from usuario_distribuidor_grupotrabajo where iduser = "+str(iduser)+""
        sqls = [delete_user_distribuidor_grupotrabajo,delete_user]
        for c in sqls:
            cursor.execute(c)
        conexxion.commit()
    delete = True
    return delete

def verificarhash(hashiduser):
    conexxion = conect()
    data = []
    with conexxion.cursor() as cursor:
        cursor.execute("select * from usuarios")
        listuser = cursor.fetchall()
        for i in listuser:
            idencode = str(i[0]).encode()
            hashIDlocal = hashlib.new("sha1",idencode)
            if hashIDlocal.hexdigest() == hashiduser:
                idsearch = i[0]
                break
            else:
                idsearch = None
    return idsearch

def consulta_actualizar(id):
    conexxion = conect()
    data = []
    with conexxion.cursor() as cursor:
        cursor.execute("select username, distribuidor, grupo_trabajo from usuarios inner join usuario_distribuidor_grupotrabajo where usuarios.iduser = usuario_distribuidor_grupotrabajo.iduser and usuarios.iduser = "+str(id)+"")
        userdata = cursor.fetchall()
        for x in userdata:
            json = {
                "username": x[0],
                "distribuidor": x[1],
                "grupotrabajo": x[2]
            }
            data.append(json)
    return data


def actualizar_usuario(id,username,distribuidor,grupotrabajo):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        try:
            update_user = "update usuarios set username='"+username+"' where iduser = "+str(id)+""
            update_user_distribuidor_gt = "update usuario_distribuidor_grupotrabajo set distribuidor='"+distribuidor+"', grupo_trabajo='"+grupotrabajo+"' where iduser = "+str(id)+""
            sqls = [update_user, update_user_distribuidor_gt]
            for c in sqls:
                cursor.execute(c)
            conexxion.commit()
            update = True
        except:
            update = False
    return update

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
