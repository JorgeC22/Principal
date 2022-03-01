from conexion import conect
import bcrypt
from models.user import User
import hashlib
import uuid
import random
import string



def insertar_usuario(username,password,DistribuidorGrupoTrabajo):
    id_usuario = str(uuid.uuid4())
    
    passencode = password.encode("utf-8")
    pass_seg_encode = bcrypt.hashpw(passencode, bcrypt.gensalt())
    pass_segura = pass_seg_encode.decode()

    ruta_usuario = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10) )
 
    
    try:
        conexxion = conect()
        with conexxion.cursor() as cursor:
            sqls = []
            insert_user = "insert into usuarios values('"+id_usuario+"','"+username+"','"+pass_segura+"')"
            sqls.append(insert_user)
            insert_user_ruta = "insert into usuario_ruta values('"+id_usuario+"','"+ruta_usuario+"')"
            sqls.append(insert_user_ruta)

            for dg in DistribuidorGrupoTrabajo:
                if dg['grupotrabajo'] != None:
                    insert_user_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo (id_usuario,distribuidor,grupo_trabajo) values('%s','%s','%s')" % (id_usuario,dg['distribuidor'],dg['grupotrabajo'])
                    sqls.append(insert_user_distribuidor_gt)
                else:
                    insert_user_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo (id_usuario,distribuidor) values('%s','%s')" % (id_usuario,dg["distribuidor"])
                    sqls.append(insert_user_distribuidor_gt)
            for c in sqls:
                cursor.execute(c)
        conexxion.commit()
        insert = True
    except:
        insert = False
        
    return insert

def relacionDistribuidroGrupoTrabajo(distribuidores,gruposTrabajos):
    datajson = []
    for number in range(0,len(distribuidores)):
        
        if gruposTrabajos[number] == "":
            json = {"distribuidor": distribuidores[number],"grupotrabajo": None}
            datajson.append(json)
        else:
            json = {"distribuidor": distribuidores[number],"grupotrabajo": gruposTrabajos[number]}
            datajson.append(json)

    return datajson





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
            idencode = i[0].encode()
            hashIDlocal = hashlib.new("sha1",idencode)
            if hashIDlocal.hexdigest() == hashiduser:
                idsearch = i[0]
                break
            else:
                idsearch = None
    return idsearch



def verificarhashrelacion(hashidrelacion):
    conexxion = conect()
    data = []
    with conexxion.cursor() as cursor:
        cursor.execute("select * from usuario_distribuidor_grupotrabajo")
        listuser = cursor.fetchall()
        for i in listuser:
            idencode = str(i[0]).encode()
            hashIDlocal = hashlib.new("sha1",idencode)
            if hashIDlocal.hexdigest() == hashidrelacion:
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
        cursor.execute("select id_distribuidor_grupotrabajo, nombre_usuario, distribuidor, grupo_trabajo from usuarios inner join usuario_distribuidor_grupotrabajo where usuarios.id_usuario = usuario_distribuidor_grupotrabajo.id_usuario and usuarios.id_usuario = '"+id+"'")
        userdata = cursor.fetchall()
        
        if len(userdata) > 1:
            
            for x in userdata:

                idRencode = str(x[0]).encode()
                hashIDrelacion = hashlib.new("sha1",idRencode)  

                if not json:
                    json = {
                    "nombreusuario": x[1],
                    "distribuidorgrupotrabajo": [{
                            "id_distribuidor_grupotrabajo": hashIDrelacion.hexdigest(),
                            "distribuidor": x[2],
                            "grupotrabajo": x[3]
                        }]
                    }
                    
                else:
                    idRencode = str(x[0]).encode()
                    hashIDrelacion = hashlib.new("sha1",idRencode)
                    grupo = {"id_distribuidor_grupotrabajo": hashIDrelacion.hexdigest(),"distribuidor": x[2],"grupotrabajo": x[3]}
                    json['distribuidorgrupotrabajo'].append(grupo)
        else:
            for x in userdata:
                idRencode = str(x[0]).encode()
                hashIDrelacion = hashlib.new("sha1",idRencode)

                json = {
                    "nombreusuario": x[1],
                    "distribuidorgrupotrabajo": {
                        "id_distribuidor_grupotrabajo": hashIDrelacion.hexdigest(),
                        "distribuidor": x[2],
                        "grupotrabajo": x[3]
                    }
                }
        
        data.append(json)
    return data


def actualizar_usuario(id,username,distribuidor,grupotrabajo):
    try:
        conexxion = conect()
        with conexxion.cursor() as cursor:
            cursor.execute("update usuarios set nombre_usuario='"+username+"' where id_usuario = '"+id+"'")

            cursor.execute("delete from usuario_distribuidor_grupotrabajo where id_usuario = '"+id+"'")

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

