import streamlit as st
import nombre_jobs

contenido_archivo = []

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

st.title('Procesamiento de Archivos .txt')

archivo = st.file_uploader("Adjuntar archivo .txt", type=["txt"])

if archivo is not None:
    try:
        # Ejecutar la función para procesar el archivo
        archivo_procesado = procesar_archivo(archivo)
        nombre_jobs.lectura_archivo(contenido_archivo)
        #nombre_jobs.ejecutar_nombre_jobs(contenido_archivo)
        st.write(contenido_archivo)
        st.write('El reporte nombre jobs se generó satisfactoriamente')
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")

