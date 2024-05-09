import re
import diccionarios


def ejecutar_stages():
    diccionario_G = diccionarios.get_g()

    encabezado = "\nNOMBRE_STAGES|CUMPLE_ESTANDAR False/True\n"
    ruta_archivo = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Proyecto_BDB.dsx'
    #salida = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/PruebaStagesSalida.csv'
    salida = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Proyecto_BDB.csv'

    nombre_links = []
    estandar_links = []
    contenido_archivo = []

    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            contenido_archivo.append(linea.strip())

    def verificar_patron(cadena, patron):
        busqueda = re.search(patron, cadena)
        if busqueda:
            return True
        else:
            return False

    def buscar_links(palabra, arreglo):
        for i, linea in enumerate(arreglo):
            if palabra in linea:
                if i + 1 < len(arreglo):
                    siguiente_linea = arreglo[i]
                    nombre_links.append(siguiente_linea[11:-1])

    busqueda_links = "StageNames"
    buscar_links(busqueda_links, contenido_archivo)

    caracteres_reemplazar = [' ','|', ',','"']

    for palabra in range(len(nombre_links)):
        for caracter in caracteres_reemplazar:
            nombre_links[palabra] = nombre_links[palabra].replace(caracter, ' ')

    for elemento in nombre_links:
        links = elemento.split()
        for nombre in links:
            estandar_links.append(nombre.strip())

    def validar_nombre(cadena, diccionario_G):
        for G in diccionario_G.keys():
            patron = r'^{}_.*'.format(re.escape(G))
            componente = verificar_patron(nombre, patron)
            if componente:
                return True
        return False

    resultados = []
    with open(salida, "a") as archivo_salida:
        archivo_salida.write(encabezado)
        for nombre in estandar_links:
            cumple_estandar = validar_nombre(nombre, diccionario_G)
            archivo_salida.write(f"{nombre}|{cumple_estandar}\n")
            resultados.append((nombre, cumple_estandar))
    return resultados

# Llamar a la función para obtener el resultado y almacenarlo en un arreglo
resultado_procesamiento = ejecutar_stages()
print(resultado_procesamiento)
print('El reporte stages se generó satisfactoriamente')
#print(resultado_procesamiento)
