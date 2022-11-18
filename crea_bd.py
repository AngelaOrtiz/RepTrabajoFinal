import os

import streamlit as st
import pandas as pd

from sqlalchemy import Column, Float, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, Session
from utils import Edu_data

# Ruta base de datos SQLlite Local.
ruta_mi_bd = os.path.abspath("./educacions.db")
mi_bd = f"sqlite:///{ruta_mi_bd}"

# Conecta a la base de datos
engine = create_engine(mi_bd, echo=True, future=True)

# Crear clase de Modelo de Datos SQLAlchemy
Base = declarative_base()

# Crear clase de Modelo de la tabla a usar
class EducacionSuperior(Base):
  # Nombre de la tabla
  __tablename__ = "EducacionSuperior"

  # Definir cada atributo de la tabla y su tipo de dato
  FID = Column(Integer, primary_key=True)
  TIPO_INSTITUCIÓN = Column(String(100))
  NOMBRE_INSTITUCIÓN = Column(String(100))
  NOMBRE_INMUEBLE = Column(String(100))
  REGIÓN = Column(String(100))
  PROVINCIA = Column(String(100))
  COMUNA = Column(String(100))
  DIRECCION = Column(String(100))
  NUMERO_DI = Column(Integer)
  LATITUD = Column(Float)
  LONGITUD = Column(Float)
  CLIMA = Column(String(100))

  def __repr__(self) -> str:
    return f" EducacionSuperior(FID={self.FID}, TIPO_INSTITUCIÓN={self.TIPO_INSTITUCIÓN}, NOMBRE_INSTITUCIÓN={self.NOMBRE_INSTITUCIÓN}, " \
      + f"NOMBRE_INMUEBLE={self.NOMBRE_INMUEBLE}, REGIÓN={self.REGIÓN}, PROVINCIA={self.PROVINCIA}, COMUNA={self.COMUNA}," \
      + f"DIRECCION={self.DIRECCION},NUMERO_DI={self.NUMERO_DI}, LATITUD={self.LATITUD}, LONGITUD={self.LONGITUD}, CLIMA={self.CLIMA}" \
      + ")"

# Crear la tabla en BD
Base.metadata.create_all(engine)
Edu = Edu_data()
Edu.to_sql(con=engine, name="EducacionSuperior", if_exists="replace", index_label="FID")

# Crear conexión a BD
# Se quita el parámetro "future=True", por compatibilidad con Pandas 1.x
engine = create_engine(mi_bd)
# Crear sesión a BD
session = Session(engine)

# Consultar por registros de algunas comunas
sql_Edu = select(EducacionSuperior)

# Consultar registros de base de datos directo desde Pandas
datos_EduSup = pd.read_sql_query(sql=sql_Edu, con=engine, index_col="FID")

#Exporta los datos a excel
datos_EduSup.to_excel("DesdeBD.xlsx")

#Exporta los datos a CSV
datos_EduSup.to_csv("DesdebaseDatos.csv",encoding="utf-8")