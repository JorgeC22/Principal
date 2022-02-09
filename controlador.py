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

def insertar_usuario(username,password):
    passencode = password.encode("utf-8")
    pass_seg_encode = bcrypt.hashpw(passencode, bcrypt.gensalt())
    pass_segura = pass_seg_encode.decode()
    conexxion = conect()
    try:
        with conexxion.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios(nombre_usuario,contraseña) VALUES('"+username+"','"+pass_segura+"')")
            conexxion.commit()
            insert = True
    except:
        insert = False
    return insert

def insertar_usuario_distribuidor_grupo(username,distribuidor,grupotrabajo):
    conexxion = conect()
    try:
        with conexxion.cursor(dictionary = True) as cursor:
            cursor.execute("SELECT * FROM usuarios where nombre_usuario = '%s'" % username)
            usuario = cursor.fetchone()

            if grupotrabajo:
                for r in grupotrabajo:
                    cursor.execute("INSERT INTO usuario_distribuidor_grupotrabajo(id_usuario,distribuidor,grupo_trabajo) VALUES(%s,'%s','%s')" % (usuario['id_usuario'],distribuidor,r))
                    conexxion.commit()
                    insert = True
            else:
                cursor.execute("INSERT INTO usuario_distribuidor_grupotrabajo(id_usuario,distribuidor,grupo_trabajo) VALUES(%s,'%s','')" % (usuario['id_usuario'],distribuidor))
                conexxion.commit()
                insert = True
    except:
        insert = False
    return insert

def obtener_usuarios():
    conexxion = conect()
    data = []
    with conexxion.cursor() as cursor:
        cursor.execute("""
                        select u.id_usuario, u.nombre_usuario, udg.distribuidor, udg.grupo_trabajo
                        from usuarios u 
	                        join usuario_distribuidor_grupotrabajo udg on u.id_usuario = udg.id_usuario""")
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
                        "nombre_usuario": i[1],
                        "distribuidor": i[2],
                        "grupotrabajo": gtrabajo
                    }
            data.append(json)
    return data

def eliminar_usuario(id_usuario):
    conexxion = conect()
    with conexxion.cursor(dictionary = True) as cursor:
        cursor.execute(""" SELECT udg.distribuidor
                            FROM usuarios u 
	                            join usuario_distribuidor_grupotrabajo udg on u.id_usuario = udg.id_usuario  
                            WHERE u.id_usuario = %s""" % id_usuario)
        distribuidor = cursor.fetchone()

        cursor.execute("""SELECT u.id_usuario, u.nombre_usuario, udg.distribuidor, udg.grupo_trabajo 
                            FROM usuarios u 
	                            join usuario_distribuidor_grupotrabajo udg on u.id_usuario = udg.id_usuario  
                            WHERE udg.distribuidor  = '%s'""" % distribuidor)
        registros = cursor.fetchall()

        if registros == []:
            cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s" %registros['id_usuario'])
        else:
            cursor.execute("DELETE FROM usuario_distribuidor_grupotrabajo WHERE  = ")


        '''
        delete_user = "delete from usuarios where id_usuario = "
        delete_user_distribuidor_grupotrabajo = "delete from usuario_distribuidor_grupotrabajo where id_usuario = "+iduser+""
        sqls = [delete_user_distribuidor_grupotrabajo,delete_user]
        for c in sqls:
            cursor.execute(c)
        conexxion.commit()
        '''
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
        cursor.execute("""
            select u.nombre_usuario, udg.distribuidor, udg.grupo_trabajo 
            from usuarios u 
                inner join usuario_distribuidor_grupotrabajo udg on u.id_usuario = udg.id_usuario  
            where u.id_usuario = %s""" % id)
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
            update_user = "update usuarios set nombre_usuario ='"+username+"' where id_usuario = "+id+""
            update_user_distribuidor_gt = "update usuario_distribuidor_grupotrabajo set distribuidor='"+distribuidor+"', grupo_trabajo='"+grupotrabajo+"' where id_usuario = "+ id +""
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
