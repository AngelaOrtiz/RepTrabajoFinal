import streamlit as st
import pandas as pd

import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt


# Se importan funcionalidades desde librería propia
from Req import Edu_data

# Obtener datos desde cache
Edu_Sup = Edu_data()

# Generar listado de comunas ordenadas
reg_puntos = Edu_Sup["REGIÓN"].sort_values().unique()

# Titulo de la pagina
st.title('Mapa de calor de instituciones según su ubicación geográfica')
st.write('Aplica los filtros a tu izquierda para filtrar el mapa por región')

with st.sidebar:
  st.write("# Filtros de Información")
  st.write("---")

  # Multiselector de comunas
  reg_sel = st.multiselect(
    label="Seleccionar por región",
    options=reg_puntos,
    default="REGIÓN DEL BIOBÍO",
  )
  # Se establece la lista completa en caso de no seleccionar ninguna
  if not reg_sel:
    reg_sel = reg_puntos.tolist()

  
# Aplicar Filtros
geo_data = Edu_Sup.query("REGIÓN==@reg_sel")

if geo_data.empty:
  # Advertir al usuario que no hay datos para los filtros
  st.warning("#### No hay registros para los filtros usados!!!")


else:
  # Desplegar Mapa
  # Obtener el punto promedio entre todas las georeferencias
  avg_lat = np.average(geo_data["LATITUD"])
  avg_lng = np.average(geo_data["LONGITUD"])

  puntos_mapa = pdk.Deck(
      map_style=None,
      initial_view_state=pdk.ViewState(
          latitude=avg_lat,
          longitude=avg_lng,
          zoom=6,
          min_zoom=10,
          max_zoom=15,
          pitch=0,
      ),
      layers=[
        pdk.Layer(
          "HeatmapLayer",
          data=geo_data,
          pickable=True,
          auto_highlight=True,
          get_position='[LONGITUD, LATITUD]',
          opacity=0.5,
        )      
      ],
      tooltip={
        "html": "<b>Tipo de institución: </b> {TIPO_INSTITUCIÓN} <br /> "
                "<b>Nombre institución: </b> {NOMBRE_INSTITUCIÓN} <br /> "
                "<b>Nombre Segundario: </b> {NOMBRE_INMUEBLE} <br /> "
                "<b>Dirección: </b> {DIRECCION} {NUMERO_DI},{COMUNA},{PROVINCIA} <br /> "
                "<b>Región: </b> {REGIÓN} <br />"
                "<b>Clima: </b> {CLIMA}<br /> ",
        "style": {
          "backgroundColor": "steelblue",
          "color": "white"
        }
      }
  )

  st.write(puntos_mapa)

Sup_Columnas = geo_data[["TIPO_INSTITUCIÓN","NOMBRE_INSTITUCIÓN","NOMBRE_INMUEBLE","DIRECCION","NUMERO_DI","COMUNA","REGIÓN","CLIMA"]]



# Titulo del data frame a mostrar
st.title('Datos de las instituciones mostradas en el mapa')
# Display an interactive table
st.write(Sup_Columnas) # preferably yields a single row