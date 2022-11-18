import streamlit as st

import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt

# Se importan funcionalidades desde librería propia
from Req import Edu_data

# Titulo de la pagina
st.title('Gráficos de instituciones según la región seleccionada')
st.write('Utiliza los filtros a tu izquierda para seleccionar tu región de interés.')

# Obtener datos desde cache
data_puntos = Edu_data()

# Generar listado de regiones ordenados
Reg_puntos = data_puntos["REGIÓN"].sort_values().unique()

# Generar listado de tipos de instituciones ordenadas
Tip_puntos = data_puntos["TIPO_INSTITUCIÓN"].sort_values().unique()

with st.sidebar:
  st.write("## Filtros de Información")
  st.write("---")

  # Multiselector de regiones
  Reg_sel = st.multiselect(
    label="Escoja una región",
    options=Reg_puntos,
    default=[]
  )
  # Se establece la lista completa en caso de no seleccionar ninguna
  if not Reg_sel:
    Reg_sel = Reg_puntos.tolist()

  # Multiselector de horarios
  Tip_sel = st.multiselect(
    label="Tipos de institución",
    options=Tip_puntos,
    default=Tip_puntos
  )
  # Se establece la lista completa en caso de no seleccionar ninguna
  if not Tip_sel:
    Tip_sel = Tip_puntos.tolist()


col_bar, col_line, col_pie = st.columns(3, gap="small")

geo_data = data_puntos.query("REGIÓN==@Reg_sel and TIPO_INSTITUCIÓN==@Tip_sel")
group_reg = geo_data.groupby(["TIPO_INSTITUCIÓN"]).size()
# Se ordenan de mayor a menor, gracias al uso del parámetros "ascending=False"
group_reg.sort_values(axis="index", ascending=False, inplace=True)

def formato_porciento(dato: float):
  return f"{round(dato, ndigits=2)}%"

with col_bar:
  bar = plt.figure()
  group_reg.plot.bar(
    title="Cantidad de instituciones por tipo",
    label="Total de Puntos",
    xlabel="Tipos de institución",
    ylabel="Cantidad",
    color="lightblue",
    grid=True,
  ).plot()
  st.pyplot(bar)

with col_line:
  line = plt.figure()
  group_reg.plot.line(
    title="Cantidad de instituciones por tipo",
    label="Total de Puntos",
    xlabel="Tipos de institución",
    ylabel="Cantidad",
    color="lightblue",
    grid=True
  ).plot()
  st.pyplot(line)

with col_pie:
  pie = plt.figure()
  group_reg.plot.pie(
    y="index",
    title="Cantidad de instituciones por tipo",
    legend=None,
    autopct=formato_porciento
  ).plot()
  st.pyplot(pie)
