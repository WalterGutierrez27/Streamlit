import streamlit as st
import nombre_jobs
import nombre_links
import nombre_stages

#ruta_archivo = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Proyecto_BDB.dsx'

def procesar_archivo(archivo):
    # Intentar leer el contenido del archivo con diferentes codificaciones
    codificaciones = ["utf-8", "latin1"]
    contenido = None
    for codificacion in codificaciones:
        try:
            contenido = archivo.read().decode(codificacion)
            contenido_archivo.append(contenido.strip())
            #st.write("Contenido del archivo:")
            #st.write(contenido)
            break
        except UnicodeDecodeError:
            pass

st.title('Procesamiento de Archivos .dsx')

ruta_archivo = st.file_uploader("Adjuntar archivo .txt", type=["dsx"])

contenido_archivo = []

with open(ruta_archivo, 'r') as archivo:
    for linea in archivo:
         contenido_archivo.append(linea.strip())

nombre_jobs.ejecutar_nombre_jobs(contenido_archivo)
nombre_stages.ejecutar_stages(contenido_archivo)
nombre_links.ejecutar_nombre_links(contenido_archivo)
