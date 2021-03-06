from camunda.client.engine_client import EngineClient
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import uuid
import requests
import json
#ec2-54-188-33-247.us-west-2.compute.amazonaws.com:8080/

host = "ec2-3-13-107-86.us-east-2.compute.amazonaws.com:8001"

def inicioProceso(json_data):
    baseUrl = "http://"+host+"/engine-rest/process-definition/key/Process_0w2618a/start"
    data = {
        "variables": json_data
    }
    print(data)

    for d in data['variables']:
        var = {"value": data['variables'][d],"type": "string"}
        data['variables'][d] = var

    respuesta = requests.post(baseUrl, json=data)
    instanciaProceso = respuesta.json()
    print(instanciaProceso)

    


def getProcesos():
    baseUrl = "http://"+host+"/engine-rest/process-instance"
    data ={
        "processDefinitionKey":"validando_de_datos"
    }
    respuesta = requests.post(baseUrl, json=data)
    procesos_json = respuesta.json()
    return procesos_json


def getVariablesProceso(idproceso):
    baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(idproceso)+"/variables"
    respuesta = requests.get(baseUrl)
    variables_json = respuesta.json()
    data = {
        "idproceso": ""+idproceso,
        "nombre": variables_json['nombre']['value'],
        "paterno": variables_json['paterno']['value'],
        "materno": variables_json['materno']['value'],
        "empresa": variables_json['empresa']['value']
    }
    return data

def getlistVariablesProceso(procesos):
    #print(procesos)
    listVarProcesos = []
    for p in procesos:
        #print(p['id'])
        baseUrl = "http://"+host+"/engine-rest/process-instance/"+str(p['id'])+"/variables"
        respuesta = requests.get(baseUrl)
        variables_json = respuesta.json()
        data = {
            "idproceso": ""+p['id'],
            "nombre": variables_json['nombre']['value'],
            "paterno": variables_json['paterno']['value'],
            "materno": variables_json['materno']['value'],
            "empresa": variables_json['empresa']['value']
        }
        listVarProcesos.append(data)
    return listVarProcesos

"""
def getactividadProceso(procesos):
    listProcesos = []
    for p in procesos:
        print(p['idproceso'])
        baseUrl = "http://ec2-34-219-25-157.us-west-2.compute.amazonaws.com:8080/engine-rest/process-instance/"+str(p['idproceso'])+"/activity-instances"
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

def CompleteTask(idtask,data):
    baseUrl = "http://"+host+"/engine-rest/task/"+str(idtask)+"/complete"
    data = {
    "variables": {
            "nombre": {
                "value": data['nombre']
            },
            "paterno": {
                "value": data['paterno']
            },
            "materno": {
                "value": data['materno']
            },
            "verificacion": {
                "value": ""+data['empresa']
            },
            "empresa": {
                "value": ""+data['empresa']
            },
            "verificacion": {
                "value": ""+data['verificacion']
            }
        }
    }
    respuesta = requests.post(baseUrl, json=data)

    print("La respuesta del servidor es: ")
    print(f"Tarea  Completado: {idtask}")



def jsonParametros(idproceso,nombre,paterno,materno,empresa,verificacion):
    json = {
        "idproceso": idproceso,
        "nombre": nombre,
        "paterno": paterno,
        "materno": materno,
        "empresa": empresa,
        "verificacion": verificacion,
    }
    return json