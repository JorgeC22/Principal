from platform import processor
from unicodedata import name
from camunda.client.engine_client import EngineClient
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import uuid
import requests
import json


def inicioProceso(nombre,aPaterno,aMaterno,empresa):
    client = EngineClient()
    resp_json = client.start_process(process_key="validacion_de_datos", 
        variables={"nombre": nombre, "paterno": aPaterno, "materno": aMaterno, "empresa": empresa}, tenant_id="", business_key="")
    idproceso = resp_json['id']
    print(idproceso)
    return idproceso

def getProcesos():
    baseUrl = "http://localhost:8080/engine-rest/process-instance"
    data ={
        "processDefinitionId":"validacion_de_datos:2:d83aba69-b5dd-11ec-b2b1-b05adacf4ec1"
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
    print(procesos)
    listVarProcesos = []
    for p in procesos:
        print(p['id'])
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

def gettask(idproceso):
    baseUrl = "http://localhost:8080/engine-rest/task?processInstanceId="+str(idproceso)+""
    respuesta = requests.get(baseUrl)
    como_json = respuesta.json()
    print(como_json)
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
                "value": ""+data['verificacion']
            }
        }
    }
    respuesta = requests.post(baseUrl, json=data)

    print("La respuesta del servidor es: ")
    print("Proceso Completado")

default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 5000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30
}

def handle_task(task: ExternalTask) -> TaskResult:
    # add your business logic here
    # get the process variable 'score'
    nombre = task.get_variable("nombre")
    empresa = task.get_variable("empresa")
    print("Bienvenido "+nombre+" de "+empresa)
    if nombre == "alberto":
        return print("Exit")
        #task.complete({"var1": 1, "var2": 2})
    else:
        return print("No contiene la variable correcta")        


def taskexternall():
    ExternalTaskWorker(worker_id="1", config=default_config).subscribe("chargeVar", handle_task)
    return True

