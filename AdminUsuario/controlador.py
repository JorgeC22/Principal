from dis import dis
from conexion import conect
import bcrypt
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
                        select u.id_usuario, u.nombre_usuario, u.contraseña, udg.id_distribuidor_grupotrabajo, udg.distribuidor, udg.grupo_trabajo, ur.ruta 
                        from usuarios u 
	                        join usuario_ruta ur on u.id_usuario  = ur.id_usuario 
	                        join usuario_distribuidor_grupotrabajo udg on ur.id_usuario = udg.id_usuario""")
        usuarios = cursor.fetchall()
        for i in usuarios:
            if(i[5]==None):
                gtrabajo = " " 
            else:
                gtrabajo = i[5]

            idUserencode = str(i[0]).encode()
            hashID = hashlib.new("sha1",idUserencode)

            idDGTencode = str(i[3]).encode()
            hashIDDGT = hashlib.new("sha1",idDGTencode)
            json = {
                        "id_distribuidor_grupotrabajo": hashIDDGT.hexdigest(),
                        "id_usuario": hashID.hexdigest(),
                        "nombre_usuario": i[1],
                        "contraseña": i[2],
                        "distribuidor": i[4],
                        "grupotrabajo": gtrabajo,
                        "ruta": i[6]
                    }
            data.append(json)
    return data

def eliminar_usuario(iduser):
    try:
        conexxion = conect()
        with conexxion.cursor() as cursor:
            delete_usuario = "delete from usuarios where id_usuario = '"+str(iduser)+"'"
            delete_usuario_distribuidor_grupotrabajo = "delete from usuario_distribuidor_grupotrabajo where id_usuario = '"+str(iduser)+"'"
            delete_usuario_ruta = "delete from usuario_ruta where id_usuario = '"+str(iduser)+"'"
            sqls = [delete_usuario_ruta,delete_usuario_distribuidor_grupotrabajo,delete_usuario]
            for c in sqls:
                cursor.execute(c)
            conexxion.commit()
        delete = True
    except:
        delete = None  
    return delete

def elimniar_distribuidor_grupotrabajo(id_distribuidor_grupotrabajo):
    sqls = []
    conexxion = conect()
    with conexxion.cursor() as cursor:
        delete_usuario_distribuidor_grupotrabajo = "delete from usuario_distribuidor_grupotrabajo where id_distribuidor_grupotrabajo = "+str(id_distribuidor_grupotrabajo)+""
        sqls.append(delete_usuario_distribuidor_grupotrabajo)
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


def IDDistribuidroGrupoTrabajo(Ids,distribuidores,gruposTrabajos):
    datajson = []
    for number in range(0,len(distribuidores)):
        id_dgt_original = verificarhashrelacion(Ids[number])
        
        if gruposTrabajos[number] == "":
            json = {"distribuidor": distribuidores[number],"grupotrabajo": None, "idDistribuidorGrupotrabajo": id_dgt_original}
            datajson.append(json)
        else:
            json = {"distribuidor": distribuidores[number],"grupotrabajo": gruposTrabajos[number],"idDistribuidorGrupotrabajo": id_dgt_original}
            datajson.append(json)

    return datajson


def verificacion_eliminacion_reg_distribuidor_grupotrabajo(idusuario,distgrupotID):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        cursor.execute("select id_distribuidor_grupotrabajo from usuario_distribuidor_grupotrabajo where id_usuario = '"+idusuario+"'")
        userdata = cursor.fetchall()

        for q in userdata:
            for reg in distgrupotID:
                print(str(q[0])+" vs "+str(reg['idDistribuidorGrupotrabajo']))
                if q[0] == reg['idDistribuidorGrupotrabajo']:
                    existencia = True
                    break
                else:
                    existencia = False
            
            if existencia == False:
                cursor.execute("delete from usuario_distribuidor_grupotrabajo where id_distribuidor_grupotrabajo = "+str(q[0])+"")
    conexxion.commit()
    return "Verificacion y eliminacion de registros realizado correctamente"

def consulta_actualizar(id_distribuidor_grupotrabajo):
    conexxion = conect()
    data = []
    json = {}
    with conexxion.cursor() as cursor:
        cursor.execute("select id_distribuidor_grupotrabajo, nombre_usuario, distribuidor, grupo_trabajo from usuarios inner join usuario_distribuidor_grupotrabajo where usuarios.id_usuario = usuario_distribuidor_grupotrabajo.id_usuario and usuario_distribuidor_grupotrabajo.id_distribuidor_grupotrabajo = "+str(id_distribuidor_grupotrabajo)+"")
        userdata = cursor.fetchall()
        
        
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



def actualizar_distribuidor_grupotrabajo(id_distribuidor_grupotrabajo,distribuidor,grupotrabajo):
    try:
        sqls = []
        conexxion = conect()
        with conexxion.cursor() as cursor:

            if grupotrabajo != "":
                update_distribuidor_grupotrabajo = "update usuario_distribuidor_grupotrabajo set distribuidor='"+distribuidor+"', grupo_trabajo= '"+grupotrabajo+"' where id_distribuidor_grupotrabajo = "+str(id_distribuidor_grupotrabajo)+""
                sqls.append(update_distribuidor_grupotrabajo)
            else:
                update_distribuidor_grupotrabajo = "update usuario_distribuidor_grupotrabajo set distribuidor='"+distribuidor+"', grupo_trabajo= Null where id_distribuidor_grupotrabajo = "+str(id_distribuidor_grupotrabajo)+""
                sqls.append(update_distribuidor_grupotrabajo)
            for accion in sqls:
                cursor.execute(accion)  
        conexxion.commit()
        update = True
    except:
        update = False

    return update











def existencia_usuario(nombre_usuario):
    conexxion = conect()
    with conexxion.cursor() as cursor:
        cursor.execute("select * from usuarios where nombre_usuario = '"+nombre_usuario+"'")
        userdata = cursor.fetchall()
        if userdata:
            for usuario in userdata:
                id_usuario = usuario[0]
        else:
            id_usuario = None
    
    return id_usuario
        

def consulta_usuario(idUsuario):
    conexxion = conect()
    data = []
    json = {}
    with conexxion.cursor() as cursor:
        cursor.execute("""
                        select u.id_usuario, u.nombre_usuario, udg.id_distribuidor_grupotrabajo, udg.distribuidor, udg.grupo_trabajo, ur.ruta 
                        from usuarios u 
	                        join usuario_ruta ur on u.id_usuario  = ur.id_usuario 
	                        join usuario_distribuidor_grupotrabajo udg on ur.id_usuario = udg.id_usuario
                        where u.id_usuario = '%s'""" % idUsuario)
        userdata = cursor.fetchall()
        
        
        if len(userdata) > 1:
            
            for x in userdata:

                idUsuario = str(x[0]).encode()
                hashIDusuario = hashlib.new("sha1",idUsuario)
                
                idDGTencode = str(x[2]).encode()
                hashIDDGT = hashlib.new("sha1",idDGTencode)  

                if not json:
                    json = {
                    "id_usuario": hashIDusuario.hexdigest(),
                    "nombreusuario": x[1],
                    "distribuidorgrupotrabajo": [{
                            "id_distribuidor_grupotrabajo": hashIDDGT.hexdigest(),
                            "distribuidor": x[3],
                            "grupotrabajo": x[4]
                        }],
                    "ruta": x[5]
                    }
                    
                else:
                    idDGTencode = str(x[2]).encode()
                    hashIDDGT = hashlib.new("sha1",idDGTencode)
                    grupo = {"id_distribuidor_grupotrabajo": hashIDDGT.hexdigest(),"distribuidor": x[3],"grupotrabajo": x[4]}
                    json['distribuidorgrupotrabajo'].append(grupo)
        else:
            for x in userdata:
                idUsuario = str(x[0]).encode()
                hashIDusuario = hashlib.new("sha1",idUsuario)
                
                idDGTencode = str(x[2]).encode()
                hashIDDGT = hashlib.new("sha1",idDGTencode) 

                json = {
                    "id_usuario": hashIDusuario.hexdigest(),
                    "nombreusuario": x[1],
                    "distribuidorgrupotrabajo": {
                    "id_distribuidor_grupotrabajo": hashIDDGT.hexdigest(),
                        "distribuidor": x[3],
                        "grupotrabajo": x[4]
                    },
                    "ruta": x[5]
                }
        
        data.append(json)
    return data


def actualizar_usuario(id,username,distgrupotID,ruta):
    sqls = []
    conexxion = conect()
    with conexxion.cursor() as cursor:
        update_usuario = "update usuarios set nombre_usuario='"+username+"' where id_usuario = '"+id+"'"
        sqls.append(update_usuario)

        update_usuario = "update usuario_ruta set ruta='"+ruta+"' where id_usuario = '"+id+"'"
        sqls.append(update_usuario)

        for reg in distgrupotID:
            if reg['idDistribuidorGrupotrabajo'] != None:
                if reg['grupotrabajo'] != None:
                    update_distribuidor_gt = "update usuario_distribuidor_grupotrabajo set distribuidor='"+reg['distribuidor']+"', grupo_trabajo='"+reg['grupotrabajo']+"' where id_distribuidor_grupotrabajo = "+str(reg['idDistribuidorGrupotrabajo'])+""
                    sqls.append(update_distribuidor_gt)
                else:
                    update_distribuidor_gt = "update usuario_distribuidor_grupotrabajo set distribuidor='"+reg['distribuidor']+"', grupo_trabajo= Null where id_distribuidor_grupotrabajo = "+str(reg['idDistribuidorGrupotrabajo'])+""
                    sqls.append(update_distribuidor_gt)
            else:
                if reg['grupotrabajo'] != None:
                    insert_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo (id_usuario,distribuidor,grupo_trabajo) values('"+id+"','"+str(reg['distribuidor'])+"','"+reg['grupotrabajo']+"')"
                    sqls.append(insert_distribuidor_gt)
                else:
                    insert_distribuidor_gt = "insert into usuario_distribuidor_grupotrabajo (id_usuario,distribuidor) values('"+id+"','"+str(reg['distribuidor'])+"')"
                    sqls.append(insert_distribuidor_gt)
        for accion in sqls:
            cursor.execute(accion)  
    conexxion.commit()
    update = True

    return update
