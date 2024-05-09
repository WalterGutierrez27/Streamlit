import nombre_jobs
import nombre_links
import nombre_stages

ruta_archivo = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Proyecto_BDB.dsx'

contenido_archivo = []

with open(ruta_archivo, 'r') as archivo:
    for linea in archivo:
         contenido_archivo.append(linea.strip())

nombre_jobs.ejecutar_nombre_jobs(contenido_archivo)
nombre_stages.ejecutar_stages(contenido_archivo)
nombre_links.ejecutar_nombre_links(contenido_archivo)
