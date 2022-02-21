import http.client
import json
from conexionBD import *
from models.reportetransaccion import reportetransaccion
from datetime import datetime
import requests
import urllib.parse
from accesos_inntec import accesos_inntec


urlbase = "https://api.alquimiadigital.mx/index.php/api"


#=============================Validar tarjeta destino========================
def cuentaDestinoActiva(reporte): 
    now = datetime.now()
    try:
        reportTrans = reporte 
        cur = conexionBDAlquimia()
        cur.execute(
            """
            select cac.id_producto_ahorro_empresa,
                cac.no_cuenta,
                cac.activo,
                camp.no_cuenta_medio_pago,
                camp.cuenta_eje 
            from cuenta_ahorro_cliente cac 
                join cuenta_ahorro_medio_pago camp on cac.id_cuenta_ahorro = camp.id_cuenta_ahorro 
            where cac.activo = 0 and camp.no_cuenta_medio_pago = '"""+str(reportTrans.tarjeta_destino)+"""'
            """
            )
        record = cur.fetchone()
        cur.close()
        flagCuentaDestino = False
        if record != None:
            reportTrans.evento = "Validacion No. Tarjeta Destino"
            reportTrans.respuesta_evento = "Satisfactorio"
            reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
            conexxion = conexionBD()
            with conexxion.cursor() as cursor:
                cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
            conexxion.commit()
            flagCuentaDestino = True
        else:
            reportTrans.evento = "Validacion No. Tarjeta Destino"
            reportTrans.respuesta_evento = "No Satisfactorio"
            reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
            conexxion = conexionBD()
            with conexxion.cursor() as cursor:
                cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
            conexxion.commit()
            flagCuentaDestino = False
        return flagCuentaDestino
    except:
        reportTrans.evento = "Validacion No. Tarjeta Destino"
        reportTrans.respuesta_evento = "No Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()
        #print(f"Error en consulta a base de datos: {e}")
        flagCuentaDestino = False
        return flagCuentaDestino



#=============================Funciones API Inntec========================

def obtenertokenAPIinntec(reporte):
    reportTrans = reporte    
    now = datetime.now()

    try:
        url = urlbase + "/oauth2/token"
        payload = "grant_type=password&username=jcrivera2&password=^K5R,*!TQ8v634E`S5&client_id=testclient&client_secret=testpass"
        headersToken = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Authorization': "Basic dGVzdGNsaWVudDp0ZXN0cGFzcw==",
            'cache-control': "no-cache"
            }
        response = requests.request("POST", url, data=payload, headers=headersToken)
        jsonA = json.loads(response.text)
        #print(jsonA)
        tokenInntec = jsonA["access_token"]
    

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
        return False



def ValidacionTarjetaOrigen(reporte):
    reportTrans = reporte
    now = datetime.now()
    try:
        conexxion = conexionBD()
        with conexxion.cursor() as cursor:

            cursor.execute("select idInntec, idTarjeta from tarjetas_inntec where numerotarjeta = "+str(reportTrans.tarjeta_origen)+"")
            respuesta_validacion = cursor.fetchall()
            if respuesta_validacion != None:
                for x in respuesta_validacion:
                    valtarjeta = {
                        "idInntec": x[0],
                        "id_tarjeta": x[1]
                    }
                    break
                reportTrans.evento = "Validacion No. Tarjeta Origen"
                reportTrans.respuesta_evento = "Satisfactorio"
                reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
            else:
                reportTrans.evento = "Validacion Tarjeta Origen"
                reportTrans.respuesta_evento = "No Satisfactorio"
                reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
                valtarjeta = False

        conexxion.commit()
        return valtarjeta

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


def obtenerCredenciales(valTarjetaorigen):
    try:
        credenciales = accesos_inntec
        for x in credenciales:
            if valTarjetaorigen['idInntec'] == x['client_id']:
                credTarjeta = {
                    "usuario": x['username'],
                    "password": x['password'],
                    "client_id_secret": x['client_id'],
                    "client_secret_empresa": x['client_secret'],
                    "client_id": x['client_id'],
                    "nombre_empresa": x['empresa'],
                    "producto_id": x['producto_id']
                }
                break
            else:
                credTarjeta = False

        return credTarjeta
    except:
        return False

def validacionSaldoInntec(token,credenciales,valTarjetaorigen,reportTrans):
    now = datetime.now()

    url = urlbase + "/tarjetasv1/tarjetaoperadora-saldo-tarjeta"
    headers = {
        'Authorization': "Bearer "+token,
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }
    payload = "proveedor=1&dispositivo=Alquimia&tipo_dispositivo=1&adicionales=%7Bnull%7D&usuario="+credenciales.get("usuario")\
                +"&password="+urllib.parse.quote(credenciales.get("password"))+"&client_id_secret="+credenciales.get("client_id_secret")\
                +"&client_secret_empresa="+credenciales.get("client_secret_empresa")\
                +"&producto_id="+credenciales.get("producto_id")+"&cliente_id="+credenciales.get("client_id")+"&id_tarjeta="+str(valTarjetaorigen['id_tarjeta'])
    #print(payload)
    response = requests.request("POST", url, data=payload, headers=headers)
    respuesta = json.loads(response.text)
    #print(respuesta)
    jsonMovimientos = respuesta["respuesta_proveedor"]["contenido"]
    print(jsonMovimientos)
    reportTrans.evento = "Validacion Saldo Inntec"
    reportTrans.respuesta_evento = "Satisfactorio"
    reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')

    print(jsonMovimientos['Saldo'])
    print(reportTrans.monto)
    if jsonMovimientos['Saldo'] >= float(reportTrans.monto):
        statussaldo = "Satisfactorio"
        print(statussaldo)
    else:
        statussaldo = "NO Satisfactorio"
        print(statussaldo)
    
    
    conexxion = conexionBD()
    with conexxion.cursor() as cursor:
        cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
    conexxion.commit()

    return statussaldo
    """except:

        reportTrans.evento = "Validacion Saldo Inntec"
        reportTrans.respuesta_evento = "No Satisfactorio"
        reportTrans.fecha_hora = now.strftime('%Y-%m-%d %H:%M:%S')

        conexxion = conexionBD()
        with conexxion.cursor() as cursor:
            cursor.execute("insert into eventos (id_transaccion,nombre_titular,num_tarjeta_origen,cvv_origen,monto,num_tarjeta_destino,evento,respuesta_evento,fecha_hora,email) values('"+reportTrans.id_transaccion+"','"+reportTrans.nombre_titular+"',"+str(reportTrans.tarjeta_origen)+","+str(reportTrans.cvv_origen)+","+str(reportTrans.monto)+","+str(reportTrans.tarjeta_destino)+",'"+reportTrans.evento+"','"+reportTrans.respuesta_evento+"','"+str(reportTrans.fecha_hora)+"','"+str(reportTrans.email)+"')")
        conexxion.commit()
        status_saldo = "no Satisfactorio"
        return status_saldo"""


#=============================Funciones Affipay========================
def obtenertokeraffipay(reporte):
    reportTrans = reporte    
    now = datetime.now()

    try:
        conn = http.client.HTTPSConnection("sandbox-tokener.affipay-pagos.net")
        payload = 'grant_type=password&username=alberth1824@hotmail.com&password=484cf4c4623425897319cb900aabb8884976cd284e9939ad7b1a9ced55f38a46'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic Ymx1bW9uX3BheV9lY29tbWVyY2VfYXBpOmJsdW1vbl9wYXlfZWNvbW1lcmNlX2FwaV9wYXNzd29yZA=='
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