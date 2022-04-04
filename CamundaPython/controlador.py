from camunda.client.engine_client import EngineClient
from camunda.external_task.external_task import ExternalTask, TaskResult
from camunda.external_task.external_task_worker import ExternalTaskWorker
import uuid
import requests


def inicioProceso(name,age):
    client = EngineClient()
    resp_json = client.start_process(process_key="charge-var", variables={"nombre": name, "edad": age}, tenant_id="", business_key="")
    idproceso = resp_json['id']
    print(idproceso)
    print(resp_json)
    return idproceso


def getProcess(idtask):

    baseUrl = "http://localhost:8080/engine-rest/task/"+idtask+"/complete"
    

    respuesta = requests.post(baseUrl, json=datos)

    como_json = respuesta.json()
    print("La respuesta del servidor es: ")
    print(como_json)