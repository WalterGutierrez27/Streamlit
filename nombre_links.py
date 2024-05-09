import re
import diccionarios

encabezado = "\nNOMBRE_LINKS|CUMPLE_ESTANDAR False/True\n"
salida = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Proyecto_BDB.csv'

diccionario_L = diccionarios.get_l()

def ejecutar_nombre_links(archivo):
    nombre_links = []
    estandar_links = []

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

    busqueda_links = "LinkNames"
    buscar_links(busqueda_links, archivo)

    caracteres_reemplazar = [' ', '|', ',']

    for palabra in range(len(nombre_links)):
        for caracter in caracteres_reemplazar:
            nombre_links[palabra] = nombre_links[palabra].replace(caracter, ' ')

    for elemento in nombre_links:
        links = elemento.split()
        for nombre in links:
            estandar_links.append(nombre.strip())

    def validar_nombre(cadena, diccionario_L):
        for L in diccionario_L.keys():
            patron = r'^{}_.*'.format(re.escape(L))
            componente = verificar_patron(nombre, patron)
            if componente:
                return True
        return False

    resultados = []
    with open(salida, "a") as archivo_salida:
        archivo_salida.write(encabezado)
        for nombre in estandar_links:
            cumple_estandar = validar_nombre(nombre, diccionario_L)
            archivo_salida.write(f"{nombre}|{cumple_estandar}\n")
            resultados.append((nombre, cumple_estandar))
    return resultados

print('El reporte links se generó satisfactoriamente')
