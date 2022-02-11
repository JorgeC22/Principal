from calendar import c
import imp
from re import X
from turtle import update
from sqlalchemy import sql, true
from conexion import conect
import json
import bcrypt
from models.user import User
import hashlib
import uuid


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
    id_usuario = str(uuid.uuid4())
    
    passencode = password.encode("utf-8")
    pass_seg_encode = bcrypt.hashpw(passencode, bcrypt.gensalt())
    pass_segura = pass_seg_encode.decode()


 
    conexxion = conect()
    with conexxion.cursor() as cursor:
        try:
            sqls = []
            insert_user = "insert into usuarios values('"+id_usuario+"','"+username+"','"+pass_segura+"')"
            sqls.append(insert_user)
            if grupotrabajo:
                for r in grupotrabajo:
                    insert_user_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo values('%s','%s','%s')" % (id_usuario,distribuidor,r)
                    sqls.append(insert_user_distribuidor_gt)
            else:
                insert_user_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo (id_usuario,distribuidor) values('%s','%s')" % (id_usuario,distribuidor)
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
        cursor.execute("""
                        select u.id_usuario, u.nombre_usuario, u.contraseña, udg.distribuidor, udg.grupo_trabajo, ur.ruta 
                        from usuarios u 
	                        join usuario_ruta ur on u.id_usuario  = ur.id_usuario 
	                        join usuario_distribuidor_grupotrabajo udg on ur.id_usuario = udg.id_usuario""")
        usuarios = cursor.fetchall()
        for i in usuarios:
            if(i[4]==None):
                gtrabajo = " " 
            else:
                gtrabajo = i[4]

            idencode = str(i[0]).encode()
            hashID = hashlib.new("sha1",idencode)
            json = {
                        "id": hashID.hexdigest(),
                        "nombre_usuario": i[1],
                        "contraseña": i[2],
                        "distribuidor": i[3],
                        "grupotrabajo": gtrabajo,
                        "ruta": i[5]
                    }
            data.append(json)
    return data

def eliminar_usuario(iduser):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        delete_usuario = "delete from usuarios where id_usuario = "+str(iduser)+""
        delete_usuario_distribuidor_grupotrabajo = "delete from usuario_distribuidor_grupotrabajo where id_usuario = "+str(iduser)+""
        delete_usuario_ruta = "delete from usuario_ruta where id_usuario = "+str(iduser)+""
        sqls = [delete_usuario_ruta,delete_usuario_distribuidor_grupotrabajo,delete_usuario]
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
    json = {}
    with conexxion.cursor() as cursor:
        cursor.execute("select nombre_usuario, distribuidor, grupo_trabajo from usuarios inner join usuario_distribuidor_grupotrabajo where usuarios.id_usuario = usuario_distribuidor_grupotrabajo.id_usuario and usuarios.id_usuario = "+str(id)+"")
        userdata = cursor.fetchall()
        
        if len(userdata) > 1:
            for x in userdata:
                if not json:
                    json = {
                    "nombreusuario": x[0],
                    "distribuidor": x[1],
                    "grupotrabajo": [{
                            "grupo": x[2]
                        }]
                    }
                    
                else:
                    grupo = {"grupo": x[2]}
                    json['grupotrabajo'].append(grupo)
        else:
            for x in userdata:
                json = {
                    "nombreusuario": x[0],
                    "distribuidor": x[1],
                    "grupotrabajo": x[2]
                }
        
        data.append(json)
    return data


def actualizar_usuario(id,username,distribuidor,grupotrabajo):
    try:
        conexxion = conect()
        with conexxion.cursor() as cursor:
            cursor.execute("update usuarios set nombre_usuario="+username+" where id_usuario = "+str(id)+"")
            if not grupotrabajo:
                cursor.execute("insert into usuario_distribuidor_grupotrabajo (id_usuario,distribuidor) values('%s','%s')" % (id,distribuidor))
            else:
                for dato in grupotrabajo:
                    cursor.execute("insert into usuario_distribuidor_grupotrabajo values('%s','%s','%s')" % (id,distribuidor,dato))
        
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
