from datetime import datetime
from os.path import isdir
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import requests

@st.cache
def Edu_data():
   # lee excel de datos de educacion superior
    Data_Sup = pd.read_excel("EducacionSuperior.xlsx", header=1, index_col="FID")

    # Se filtran columna de datos
    Sup_Columnas = Data_Sup[["TIPO_INST","NOMBRE_INS","NOMBRE_INM","REGIÓN","PROVINCIA","COMUNA","DIRECCION","NUMERO_DI","LATITUD","LONGITUD"]]

    # Se cambian nombres de columnas
    Edu_Sup = Sup_Columnas.rename(columns={
    "TIPO_INST":"TIPO_INSTITUCIÓN",
    "NOMBRE_INS": "NOMBRE_INSTITUCIÓN",
    "NOMBRE_INM": "NOMBRE_INMUEBLE",})

    #Comienza creacion de columna "FECHA_PROCESO"
    ahora=datetime.now()
    Edu_Sup["FECHA_PROCESO"]=ahora.strftime('%Y-%m-%d')

    #Crea columna vacia "CLIMA"
    Edu_Sup["CLIMA"]=""
    #print(Edu_Sup)

    #Inicia Consulta de clima
    listaComuna=Edu_Sup["COMUNA"]
    #Crea lista de comunas a partir de Excel
    comunas=[]
    for n in listaComuna:
        if n not in comunas:
            comunas.append(n)
    #print(comunas)

    ##############################################################
    #consulta clima por comuna
    load_dotenv()
    # Leer variable de API KEY desde archivo externo
    WEATHER_API_KEY="0421a6f8ec8dab9677014a8c77125650"

    # Definir lugar a consultar
    # Crear conexión a la API
    clima=[]
    for n in comunas:
        ubicacion=n+",CL"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={ubicacion}&APPID={WEATHER_API_KEY}&lang=es"
        datos = requests.get(URL)
        datos_json = datos.json()
        d=datos_json['cod']
        if(d=="404"):
            clima.append("Sin dato")
        else:
            clima.append(datos_json['weather'][0]['description'])

    #Funcion que evalua columnas para asignar clima
    def asigna_clima(data):
        comuna=data["COMUNA"]
        latitud=data["LATITUD"]
        longitud=data["LONGITUD"]
        if ((-56.5 < latitud < -17.4) and (-109.5 < longitud < -65)):
            return clima[comunas.index(comuna)]
        else:
            return "Coordenas no corresponden"

    # se asigna valores de clima a cada registro
    Edu_Sup["CLIMA"] = Edu_Sup.apply(asigna_clima, axis=1)
           
    return Edu_Sup
