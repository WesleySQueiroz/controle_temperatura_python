import requests
from datetime import datetime
import time
from time import strftime
import json

def AlertaTemperatura(valor):
    
    tempo = time.strftime('%H:%M:%S')
    data = time.strftime('%y-%m-%d')
    date = '20' + data

    valorsala = str(valor)

    API_Key = "03b8c40e20771256eec6adcf6a5dc3539cc024d9"

    headers = {"Content-Type": "application/json", "X-API-Token": API_Key}

    data = {"notification_content": {
        "name": "Aviso",
        "title": "Temperatura da sala: " + valorsala,
        "body": tempo
        }         
     }
    
    url = 'https://api.appcenter.ms/v0.1/apps/ws.queiroz/APPGerador/push/notifications'


    r = requests.post(url, headers = headers, data = json.dumps(data))
            
        

    
    
    
