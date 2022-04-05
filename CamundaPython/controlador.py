from unicodedata import name
from camunda.client.engine_client import EngineClient
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import uuid
import requests
import json


def inicioProceso(nombre,aPaterno,aMaterno):
    client = EngineClient()
    resp_json = client.start_process(process_key="validacion_de_datos", 
        variables={"nombre": nombre, "paterno": aPaterno, "materno": aMaterno}, tenant_id="", business_key="")
    idproceso = resp_json['id']
    print(idproceso)
    return idproceso


def getVariablesProceso(idproceso):
    baseUrl = "http://localhost:8080/engine-rest/process-instance/"+str(idproceso)+"/variables"
    respuesta = requests.get(baseUrl)
    variables_json = respuesta.json()
    data = {
        "idproceso": ""+idproceso,
        "nombre": variables_json['nombre']['value'],
        "paterno": variables_json['paterno']['value'],
        "materno": variables_json['materno']['value']
    }
    return data

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