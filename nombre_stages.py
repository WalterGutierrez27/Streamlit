import re
import diccionarios

encabezado = "\nNOMBRE_STAGES|CUMPLE_ESTANDAR False/True\n"
salida = 'C:/Users/waltergutierrez/OneDrive - SETI S.A.S/SETI/OKRS 2024/Desarrollo Insignias Python/Python/Entrada/Proyecto_BDB.csv'

diccionario_G = diccionarios.get_g()

def ejecutar_stages(archivo):
    nombre_stages = []
    estandar_stages = []

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
                    nombre_stages.append(siguiente_linea[11:-1])

    busqueda_stages = "StageNames"
    buscar_links(busqueda_stages, archivo)

    caracteres_reemplazar = [' ','|', ',','"']

    for palabra in range(len(nombre_stages)):
        for caracter in caracteres_reemplazar:
            nombre_stages[palabra] = nombre_stages[palabra].replace(caracter, ' ')

    for elemento in nombre_stages:
        links = elemento.split()
        for nombre in links:
            estandar_stages.append(nombre.strip())

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
        for nombre in estandar_stages:
            cumple_estandar = validar_nombre(nombre, diccionario_G)
            archivo_salida.write(f"{nombre}|{cumple_estandar}\n")
            resultados.append((nombre, cumple_estandar))
    return resultados

print('El reporte stages se generó satisfactoriamente')
