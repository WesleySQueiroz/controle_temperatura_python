# -*- coding: utf-8 -*-
import os
import requests
import re


try:
   r = requests.get('http://www.acessoseg.com.br/webserviceacseg/api/LogDesligar')
except Exception:
   print('Falha de Conexão')



os.system('sudo shutdown -r now')
       
