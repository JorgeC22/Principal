import http.client
import json
from conexionBD import conexionBD
from models.reportetransaccion import reportetransaccion
from datetime import datetime
import requests
import urllib.parse
import accesos_inntec

now = datetime.now()
urlbase = "https://api.alquimiadigital.mx/index.php/api"

def obtenertokenAPIinntec(reporte):
    reportTrans = reporte    

    try:
        


        reportTrans.evento = "Token APIInntec autenticacion"
        reportTrans.respuesta_evento = "Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')

        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()

    
        return tokenInntec
    except:
        reportTrans.evento = "Token APIInntec autenticacion"
        reportTrans.respuesta_evento = "No Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()
        return "NO token"



def obtenertokeraffipay(reporte):
    reportTrans = reporte    

    try:
        conn = http.client.HTTPSConnection("sandbox-tokener.affipay-pagos.net")
        payload = 'grant_type=password&username=&password='
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic '
        }
        conn.request("POST", "/oauth/token", payload, headers)
        res = conn.getresponse()
        data = res.read()
        datadecode = data.decode("utf-8")
        jsondata = json.loads(datadecode)
        token = jsondata["access_token"]


        reportTrans.evento = "Token Affipay autenticacion"
        reportTrans.respuesta_evento = "Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')

        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()

    
        return token
    except:
        reportTrans.evento = "Token Affipay autenticacion"
        reportTrans.respuesta_evento = "No Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()
        return "NO token"


def ValidacionTarjetaOrigen(reportTrans):
    respuesta_validacion = []
    try:
        conexxion = conexionBD()
        with conexxion.cursor() as cursor:

            cursor.execute("select numerotarjeta from tarjetas_inntec where numerotarjeta = "+str(reportTrans.tarjeta_origen)+"")
            respuesta_validacion.append(cursor)
            if respuesta_validacion != None:
                valtarjeta = respuesta_validacion
            else:
                valtarjeta = False

            reportTrans.evento = "Validacion Tarjeta Origen"
            reportTrans.respuesta_evento = "Satisfactorio"
            reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()

    except:
        reportTrans.evento = "Validacion Tarjeta Origen"
        reportTrans.respuesta_evento = "No Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()
        valtarjeta = False

    return valtarjeta


def validacionSaldoInntec(token,credenciales,idTarjeta,reportTrans):
    
    try:

        url = urlbase + "/tarjetasv1/tarjetaoperadora-saldo-tarjeta"
        headers = {
            'Authorization': "Bearer "+token,
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }
        payload = "proveedor=1&dispositivo=Alquimia&tipo_dispositivo=1&adicionales=%7Bnull%7D&usuario="+credenciales.get("usuario")\
                    +"&password="+urllib.parse.quote(credenciales.get("password"))+"&client_id_secret="+credenciales.get("client_id_secret")\
                    +"&client_secret_empresa="+credenciales.get("client_secret_empresa")\
                    +"&producto_id="+credenciales.get("producto_id")+"&cliente_id="+credenciales.get("client_id")+"&id_tarjeta="+str(idTarjeta)
        #print(payload)
        response = requests.request("POST", url, data=payload, headers=headers)
        respuesta = json.loads(response.text)
        #print(respuesta)
        jsonMovimientos = respuesta["respuesta_proveedor"]["contenido"]
        reportTrans.evento = "Validacion Saldo Inntec"
        reportTrans.respuesta_evento = "Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()

        if jsonMovimientos['Saldo'] >= reportTrans.monto:
            
            status_saldo = True
        else:
            status_saldo = True

    except:

        reportTrans.evento = "Validacion Saldo Inntec"
        reportTrans.respuesta_evento = "No Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')

        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()
        status_saldo = False


    return status_saldo