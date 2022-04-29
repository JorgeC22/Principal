from ntpath import join
from this import d
from urllib import response
import uuid
from xmlrpc.client import boolean
import requests
import json
#ec2-54-188-33-247.us-west-2.compute.amazonaws.com:8080/

host = "localhost:8080"

def inicioProceso():
    baseUrl = "http://"+host+"/engine-rest/process-definition/key/Process_0w2618a/start"
    data = {
        "variables": {
            "datosProceso": {
                "value": "{\"documentos\": []}",
                "type": "String"
            }
        } 
    }
    #data = {
    #    "variables": json_data
    #}
    #print(data)

    #for d in data['variables']:
    #    var = {"value": data['variables'][d],"type": "string"}
    #    data['variables'][d] = var

    respuesta = requests.post(baseUrl, json=data)
    instanciaProceso = respuesta.json()
    print(instanciaProceso)



def getProcesos():
    baseUrl = "http://"+host+"/engine-rest/process-instance"
    data ={
        "processDefinitionKey":"Process_0w2618a"
    }
    respuesta = requests.post(baseUrl, json=data)
    procesos_json = respuesta.json()
    return procesos_json


def getVariablesProceso(idproceso):
    baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(idproceso)+"/variables"
    respuesta = requests.get(baseUrl)
    variables_json = respuesta.json()
    #data = {
    #    "idproceso": ""+idproceso,
    #    "nombre": variables_json['nombre']['value']
    #}
    variables_json['idproceso'] = idproceso

    return variables_json

def getlistVariablesProceso(procesos):
    #print(procesos)
    listVarProcesos = []
    for p in procesos:
        #print(p['id'])
        baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(p['id'])+"/variables"
        respuesta = requests.get(baseUrl)
        variables_json = respuesta.json()
        #data = {
        #    "idproceso": ""+p['id'],
        #    "nombre": variables_json['nombre']['value']
        #}
        variables_json['idproceso'] = p['id']
        listVarProcesos.append(variables_json)
        #print(variables_json)
    return listVarProcesos

"""
def getactividadProceso(procesos):
    listProcesos = []
    for p in procesos:
        print(p['idproceso'])
        baseUrl = "http://localhost:8080/engine-rest/process-instance/"+str(p['idproceso'])+"/activity-instances"
        respuesta = requests.get(baseUrl)
        actividades_json = respuesta.json()
        childActivityInstances = actividades_json['childActivityInstances']
        for a in childActivityInstances:
            if a['activityName'] == "Verificar Datos":
                print(childActivityInstances)
                listProcesos.append(p)
    return listProcesos
"""

def getactividadProcesos(procesos):
    listProcesos = procesos
    for p in procesos:
        #print(p['idproceso'])
        baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(p['idproceso'])+"/activity-instances"
        respuesta = requests.get(baseUrl)
        actividades_json = respuesta.json()
        childActivityInstances = actividades_json['childActivityInstances']
        for a in childActivityInstances:
            #print(childActivityInstances)
            p["tarea"] = a['activityName']
      
    return listProcesos

def getVariableJson(idproceso):
    baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(idproceso)+"/variables"
    respuesta = requests.get(baseUrl)
    variables_json = respuesta.json()
    jsons = variables_json['datosProceso']['value']
    jsons = json.loads(jsons)
    return jsons

def getProcesoActividad(data):
    Proceso = data
    #print(p['idproceso'])
    baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(Proceso['idproceso'])+"/activity-instances"
    respuesta = requests.get(baseUrl)
    actividades_json = respuesta.json()
    childActivityInstances = actividades_json['childActivityInstances']
    for a in childActivityInstances:
        #print(childActivityInstances)
        Proceso["tarea"] = a['activityName']
      
    return Proceso
#a['activityName']

def gettask(idproceso):
    baseUrl = "http://"+host+"/engine-rest/task?processInstanceId="+str(idproceso)+""
    respuesta = requests.get(baseUrl)
    como_json = respuesta.json()
    #print(como_json)
    for x in como_json:
        idtask = x['id']
 
    return idtask

def CompleteTask(idtask,dataJson):
    baseUrl = "http://"+host+"/engine-rest/task/"+str(idtask)+"/complete"
    jsonD = json.dumps(dataJson)
    #jsonD = jsonD.replace("\"", "\\\"")
    #print(jsonD)
    data = {
        "variables": {
            "datosProceso": {
                "value": ""+jsonD,
                "type": "String"
            }
        }
    }

    #for d in data['variables']:
    #    var = {"value": data['variables'][d],"type": "string"}
    #    data['variables'][d] = var
    
    #print(data)
    respuesta = requests.post(baseUrl, json=data)

    print("La respuesta del servidor es: ")
    print(f"Tarea  Completado: {idtask}")



def jsonParametros(idproceso,nombre,paterno,materno,empresa,valDocumentacion):
    json = {
        "idproceso": idproceso,
        "nombre": nombre,
        "valDocumentacion": valDocumentacion,
    }
    return json


def datosProcesos(listas,jsonData):
    print(jsonData)
    data = []
    for l in listas:
        if len(l) > 1:
            json = {
                "campo": l[0],
                "rutaS3": "https://"+l[1],
                "validacion": l[2]
            }
            data.append(json)
    
    jsonData['documentos'] = data

    #print(jsonData)
    return jsonData


############################################################################################
############################################################################################
############################################################################################

def getJsonProceso(idproceso):
    baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(idproceso)+"/variables"
    respuesta = requests.get(baseUrl)
    response = respuesta.json()
    datos_json = response['datosProceso']['value']
    datos_json = json.loads(datos_json)
    datos_json['idproceso'] = idproceso

    return datos_json

def getlistJsonProceso(procesos):
    #print(procesos)
    listJsonProcesos = []
    for p in procesos:
        #print(p['id'])
        baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(p['id'])+"/variables"
        respuesta = requests.get(baseUrl)
        response = respuesta.json()
        datos_json = response['datosProceso']['value']
        datos_json = json.loads(datos_json)
        datos_json['idproceso'] = p['id']
        listJsonProcesos.append(datos_json)
        #print(variables_json)
    return listJsonProcesos