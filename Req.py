import streamlit as st
import pandas as pd

def Edu_data():
   # lee excel de datos de educacion superior
    Edu_Sup = pd.read_excel("EducacionSuperior2.xlsx", header=0, index_col="FID")
    
    return Edu_Sup
