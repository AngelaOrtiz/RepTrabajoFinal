import streamlit as st
import streamlit.components.v1 as components

st.write("### Aplicación de ubicacion de instituciones de educación superior")
link="https://www.ide.cl/"
components.html("""
<div style="background: gray;border-radius: 2px;padding: 5px 25px;">
  <h4>
    Datos de creación de la aplicación
  </h4>
  <p>
    <b>Creado por:</b> Angela Ortiz Varela
  <p>
  </h4>
  <p>
    <b>email:</b> angelaortizvarela@gmail.com
  <p>
  </h4>
  <p>
    <b>Datos obtenidos de:</b> IDE Chile
  <p>
</div>
""",width=700, height=190)

st.write("Ingresa a la pagina de la IDE en el siguiente [link](https://www.ide.cl/)")