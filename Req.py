from datetime import datetime
from os.path import isdir
import streamlit as st
import pandas as pd
import os
import requests



def Edu_data():
   # lee excel de datos de educacion superior
    Data_Sup = pd.read_excel("EducacionSuperior2.xlsx", header=1, index_col="FID")

    # Se filtran columna de datos
    Sup_Columnas = Data_Sup[["TIPO_INST","NOMBRE_INS","NOMBRE_INM","REGIÓN","PROVINCIA","COMUNA","DIRECCION","NUMERO_DI","LATITUD","LONGITUD","CLIMA"]]

    # Se cambian nombres de columnas
    Edu_Sup = Sup_Columnas.rename(columns={
    "TIPO_INST":"TIPO_INSTITUCIÓN",
    "NOMBRE_INS": "NOMBRE_INSTITUCIÓN",
    "NOMBRE_INM": "NOMBRE_INMUEBLE",})

    return Edu_Sup
