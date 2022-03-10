import requests
import json
from enum import Enum

class ApiClient:
    apiUri = 'https://api.elasticemail.com/v2'
    apiKey = 'F6EA92D697ECC4305A6A1F7AB8013046C838DE3EF4779BAF5114979163BF52C8BE9EE7DFB56EC519C2262D357A7F7671'

    def Request(method, url, data, attachs=None):
        data['apikey'] = ApiClient.apiKey
        if method == 'POST':
            result = requests.post(ApiClient.apiUri + url, params = data, files = attachs)
        elif method == 'PUT':
            result = requests.put(ApiClient.apiUri + url, params = data)
        elif method == 'GET':
            attach = ''
            for key in data:
                attach = attach + key + '=' + data[key] + '&' 
            url = url + '?' + attach[:-1]
            result = requests.get(ApiClient.apiUri + url)    
            
        jsonMy = result.json()
        
        if jsonMy['success'] is False:
            return jsonMy['error']
            
        return jsonMy['data']

def Send(subject, EEfrom, fromName, to, bodyText, isTransactional, attachmentFiles = []):
    tmp_attachments = []
    for name in attachmentFiles:
        tmp_attachments.append(('attachments', open(name, 'rb')))
        
    return ApiClient.Request('POST', '/email/send', {
                'subject': subject,
                'from': EEfrom,
                'fromName': fromName,
                'to': to,
                'template' : 'emailSaldos',
                'bodyText': bodyText,
                'isTransactional': isTransactional}, tmp_attachments)
    
attachments = []
attachments.append('C:/Users/beto_/Documents/ServicioSocial/ProyectoPython/achr.txt')
print(Send("Prueba Archivo", "jcrivera@vitaebeneficios.com", "Vitae Travel", "jcervantes@tecnocengroup.com", "Text Body", True, attachments))