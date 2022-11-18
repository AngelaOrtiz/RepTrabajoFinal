from datetime import datetime
from os.path import isdir
import streamlit as st
import pandas as pd
import os
import requests



def Edu_data():
   # lee excel de datos de educacion superior
    Data_Sup = pd.read_excel("EducacionSuperior2.xlsx", header=0, index_col="FID")

    # Se filtran columna de datos
    Edu_Sup = Data_Sup[["TIPO_INSTITUCIÓN","NOMBRE_INSTITUCIÓN","NOMBRE_INMUEBLE","REGIÓN","PROVINCIA","COMUNA","DIRECCION","NUMERO_DI","LATITUD","LONGITUD","CLIMA"]]

    return Edu_Sup
