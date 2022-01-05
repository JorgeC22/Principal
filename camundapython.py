import requests

baseUrl = "http://localhost:8080/engine-rest/process-definition/key/payment-retrieval/start"
datos = {
	"variables": {
		"amount": {
			"value":1220,
			"type":"long"
		},
		"item": {
			"value": "item-xyz"
		}
	}
}

respuesta = requests.post(baseUrl, json=datos)

como_json = respuesta.json()
print("La respuesta del servidor es: ")
print(como_json)

id = como_json['id']
print(f"El id es: {id}")
