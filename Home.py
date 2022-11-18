import streamlit as st
import streamlit.components.v1 as components

# Se configura la página
st.set_page_config(
  page_icon=":thumbs_up:",
  layout="wide",
)
st.title('Educación Superior en Chile 🧑‍🏫')

st.write("En esta página encontraras información geográfica sobre las instituciones de educación superior de Chile.")

st.sidebar.write("## Mapas y graficos de Educación Superior")

st.write("## ¿Como es la educación superior en Chile?")
st.write("Este video te lo puede explicar")

components.html("""
  <iframe width="700" height="394" src="https://www.youtube.com/embed/ZT6cZJD84LQ?start=102" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
  </iframe>
""", height=400)

st.write("---")
st.write("## ¿Que es la gratuidad?")
st.write("Este video te lo puede explicar")

components.html("""
  <iframe width="700" height="394" src="https://www.youtube.com/embed/HI2buNUc0n4" 
  title="YouTube video player" f
  rameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""", height=400)