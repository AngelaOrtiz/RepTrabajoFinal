import streamlit as st

import pydeck as pdk
import numpy as np

# Se importan funcionalidades desde librería propia
from Req import Edu_data

Edu_Sup=Edu_data()
# Titulo de la pagina
st.title('Mapa de instituciones según su ubicación geográfica')
st.write('Aplica los filtros a tu izquierda para personalizar el mapa')

# Generar listado de Regiones ordenados
tip_puntos = Edu_Sup["TIPO_INSTITUCIÓN"].sort_values().unique()

# Generar listado de comunas ordenadas
com_puntos = Edu_Sup["COMUNA"].sort_values().unique()

with st.sidebar:
  st.write("## Filtros de Información")
  st.write("---")

  # Multiselector de comunas
  comuna_sel = st.multiselect(
    label="Seleccionar por comuna",
    options=com_puntos,
    default=[]
  )
  # Se establece la lista completa en caso de no seleccionar ninguna
  if not comuna_sel:
    comuna_sel = com_puntos.tolist()

  # Multiselector de horarios
  tip_sel = st.multiselect(
    label="Tipo de institución",
    options=tip_puntos,
    default=tip_puntos
  )
  # Se establece la lista completa en caso de no seleccionar ninguna
  if not tip_sel:
    ti_sel = tip_puntos.tolist()



# Aplicar Filtros
geo_data = Edu_Sup.query(" TIPO_INSTITUCIÓN==@tip_sel and COMUNA==@comuna_sel")

if geo_data.empty:
  # Advertir al usuario que no hay datos para los filtros
  st.warning("#### No hay registros para los filtros usados!!!")
else:
  # Desplegar Mapa
  # Obtener el punto promedio entre todas las georeferencias
  avg_lat = np.median(geo_data["LATITUD"])
  avg_lng = np.median(geo_data["LONGITUD"])

  puntos_mapa = pdk.Deck(
      map_style=None,
      initial_view_state=pdk.ViewState(
          latitude=avg_lat,
          longitude=avg_lng,
          zoom=10,
          min_zoom=4,
          max_zoom=20,
          pitch=0,
      ),
      layers=[
        pdk.Layer(
          "ScatterplotLayer",
          data=geo_data,
          pickable=True,
          auto_highlight=True,
          get_position='[LONGITUD, LATITUD]',
          filled=True,
          opacity=0.6,
          radius_scale=10,
          radius_min_pixels=5,
          get_fill_color=[255, 128, 0]
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

