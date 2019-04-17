# -*- coding: utf-8 -*-
import requests
import re


def ModuloTemperatura(valor):
    
   # print('valor antes do slice' + valor)

    
    #valor = valor[0:2]
    #print('valor modulo temperatura' + valor)

    inteiro = valor[0:2]
    decimal = valor[3:5]

    tempnova = inteiro + ',' + decimal  
    

   # print('valor temp' + tempnova)
    
    

    filtro = re.compile('([0-9]+)')
    
    temp = filtro.findall(valor)

    temperatura = temp[0:2]

    valorenvio = str(temperatura)    
    
    try:
       r = requests.get('http://www.acessoseg.com.br/webserviceacseg/api/temperatura/%s'%tempnova)
    except Exception:
       print('Falha de Conexão')
       
       
       
               



 
