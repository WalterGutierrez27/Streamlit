import re
import diccionarios
from itertools import product

encabezado = "NOMBRE_JOBS|CUMPLE_ESTANDAR False/True\n"
salida = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Proyecto_BDB.csv'

diccionario_P = diccionarios.get_p()
diccionario_T = diccionarios.get_t()

def ejecutar_nombre_jobs(archivo):
    nombre_jobs = []

    def verificar_patron(cadena, patron):
        busqueda = re.search(patron, cadena)
        if busqueda:
            return True
        else:
            return False

    def buscar_nombre_job(palabra, arreglo):
        for i, linea in enumerate(arreglo):
            if palabra in linea:
                if i + 1 < len(arreglo):
                    siguiente_linea = arreglo[i + 1]
                    nombre_jobs.append(siguiente_linea[12:-1])

    busqueda = "BEGIN DSJOB"
    buscar_nombre_job(busqueda, archivo)

    def validar_nombre(cadena, diccionario_T, diccionario_P):
        for T, P in product(diccionario_T.keys(), diccionario_P.keys()):
            patron = r'^{}_{}_.*'.format(re.escape(T), re.escape(P))
            componente = verificar_patron(nombre, patron)
            if componente:
                return True
        return False

    resultados = []
    with open(salida, "w") as archivo_salida:
        archivo_salida.write(encabezado)
        for nombre in nombre_jobs:
            cumple_estandar = validar_nombre(nombre, diccionario_T, diccionario_P)
            archivo_salida.write(f"{nombre}|{cumple_estandar}\n")
            resultados.append((nombre, cumple_estandar))
    return resultados

print('El reporte nombre jobs se generó satisfactoriamente')