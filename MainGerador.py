# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
import serial
from ModuloTemperatura import ModuloTemperatura
from ModuloAlertaTemperatura import AlertaTemperatura
from ModuloLogLigar import LogLigar
import requests

arduino = serial.Serial('/dev/ttyACM0', 9600)

def main():
    conti = 0
	
    ligar = 1
	
    while (True):
        flag = 1
        
        VALOR_RECEBIDO = arduino.readline()
        
        valor = VALOR_RECEBIDO.decode("UTF-8")
        print('valor transformado ante de float ' + valor)
        
        valorfloat = valor[0:3]
        novovalor = valor[0:5]
        #print('novo valor : ' + novovalor)
           
        sub = valor[0:1]
		
		#ModuloLigarRaspberry
            if(ligar == 1):
                LogLigar(novovalor)
                ligar = 0
						
		#ModuloTemperatura(valorfloat)
		ModuloTemperatura(novovalor)
        	
		temp = float(valorfloat)
		if(temp >= 26.00 and conti == 0):              
			if(conti != 1 and conti != 2 and conti != 3):                
			  #print(conti)
			  conti = 1
			  ModuloTemperatura(novovalor)
			  AlertaTemperatura(temp)
			  
		if(temp >= 27.00 and temp < 29.00 and conti == 1):
			if(conti != 0 and conti != 2 and conti != 3):                    
			  #print(conti)
			  conti = 2
			  ModuloTemperatura(novovalor)
			  AlertaTemperatura(temp)
			  
		if(temp >= 29.00 and temp < 31.00 and conti == 2):
			if(conti != 0 and conti != 1 and conti != 3):
			  #print(conti)
			  conti = 3
			  ModuloTemperatura(novovalor)
			  AlertaTemperatura(temp)
			  
		if(temp >= 31.00 and conti == 3):
			if(conti != 0 and conti != 1 and conti != 2): 
			  #print(conti)
			  conti = 4
			  ModuloTemperatura(novovalor)
			  AlertaTemperatura(temp)

		if(temp < 26.00):
			conti = 0		
	     


if __name__ == "__main__":
    main()
    
    
