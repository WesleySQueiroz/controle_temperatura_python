import os
import requests
import json

while(True):
   # print('reiniciar')
    r = requests.get('http://www.acessoseg.com.br/webserviceacseg/api/desligamento/')
    valor = r.text
   # print(valor)
    if(valor == '"1"'):
        r = requests.get('http://www.acessoseg.com.br/webserviceacseg/api/desligar/0')
        os.system('sudo shutdown -r now')
    
