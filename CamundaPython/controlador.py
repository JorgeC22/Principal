from platform import processor
from unicodedata import name
from camunda.client.engine_client import EngineClient
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import uuid
import requests
import json

"""
def inicioProceso(form_data,empresa):
    client = EngineClient()
    if form_data['formulario'] == "personal":
        resp_json = client.start_process(process_key="validando_de_datos", 
        variables={"nombre": form_data['nombre'], "paterno": form_data['apellidoP'], "materno": form_data['apellidoM'], "empresa": empresa, "formulario": form_data['formulario']}, tenant_id="", business_key="")
        idproceso = resp_json['id']
    elif form_data['formulario'] == "empresarial":
        resp_json = client.start_process(process_key="validando_de_datos", 
        variables={"nombre_empresa": form_data['nombre_empresa'], "mercado": form_data['mercado'], "estado": form_data['estado'], "empresa": empresa, "formulario": form_data['formulario']}, tenant_id="", business_key="")
        idproceso = resp_json['id']
    #print(idproceso)
    return idproceso
"""
def inicioProceso(json_data):
    client = EngineClient()
    resp_json = client.start_process(process_key="validando_de_datos",variables= json_data)
    idproceso = resp_json['id']
    #print(idproceso)
    return idproceso


def getProcesos():
    baseUrl = "http://localhost:8080/engine-rest/process-instance"
    data ={
        "processDefinitionKey":"validando_de_datos"
    }
    respuesta = requests.post(baseUrl, json=data)
    procesos_json = respuesta.json()
    return procesos_json


def getVariablesProceso(idproceso):
    baseUrl = "http://localhost:8080/engine-rest/process-instance/"+str(idproceso)+"/variables"
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
        baseUrl = "http://localhost:8080/engine-rest/process-instance/"+str(p['id'])+"/variables"
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
        baseUrl = "http://localhost:8080/engine-rest/process-instance/"+str(p['idproceso'])+"/activity-instances"
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
    baseUrl = "http://localhost:8080/engine-rest/process-instance/"+str(Proceso['idproceso'])+"/activity-instances"
    respuesta = requests.get(baseUrl)
    actividades_json = respuesta.json()
    childActivityInstances = actividades_json['childActivityInstances']
    for a in childActivityInstances:
        #print(childActivityInstances)
        Proceso["tarea"] = a['activityName']
      
    return Proceso
#a['activityName']

def gettask(idproceso):
    baseUrl = "http://localhost:8080/engine-rest/task?processInstanceId="+str(idproceso)+""
    respuesta = requests.get(baseUrl)
    como_json = respuesta.json()
    #print(como_json)
    for x in como_json:
        idtask = x['id']
 
    return idtask

def CompleteTask(idtask,data):
    baseUrl = "http://localhost:8080/engine-rest/task/"+str(idtask)+"/complete"
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