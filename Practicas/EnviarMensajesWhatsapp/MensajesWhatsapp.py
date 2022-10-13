from operator import concat
import pywhatkit
import xlrd
import pandas as pd
from datetime import datetime as dt
import time
import keyboard

#pywhatkit.sendwhatmsg("+573146531188", "Te amo", 14, 6, 15, True, 2)
filepath = "C:\workspace\curso-python\Practicas\EnviarMensajesWhatsapp\PlantillaEnvioMensajes.xls"
#openFile = xlrd.open_workbook(filepath)
openFile = pd.read_excel(filepath)
date = dt.now()
hora = date.time().strftime("%H:%M:%S")
#Sheet = openFile.sheet_by_name("datos")

    #print(columna, end = "\n\n")
    

#Envió de mensajes whatsapp
for index, mensaje in openFile.iterrows():
    
    concat = mensaje[0]
    columna0 = "+" + str(concat)
    columna1 = mensaje[1]
    #columna2 = mensaje[2]
    #columna3 =  mensaje[3]
    pywhatkit.sendwhatmsg(columna0, columna1, dt.now().hour, 
                          dt.now().minute + 1)#, True, 2)
    
    
    

    keyboard.press_and_release('enter')
    time.sleep(1)
    
    






