"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    with open('clusters_report.txt') as report:
        row = report.readlines()

  # las 4 tienen información que no nos sorve por lo que se limpian
    row = row[4:]
    clusters = []
    cluster = [0, 0, 0, '']

    for fila in row:
        if re.match('^ +[0-9]+ +', fila):
            number, cantidad, porcentaje, *words = fila.split()
        # casteo de datos
            cluster[0] = int(number)
            cluster[1] = int(cantidad)
            cluster[2] = float(porcentaje.replace(',','.'))
            words.pop(0)
            words = ' '.join(words)
            cluster[3] += words

        elif re.match('^\n', fila) or re.match('^ +$', fila):
            cluster[3] = cluster[3].replace('.', '')
            clusters.append(cluster)
            cluster = [0, 0, 0, '']

        elif re.match('^ +[a-z]', fila):
            words = fila.split()
            words = ' '.join(words)
            cluster[3] += ' ' + words
    df = pd.DataFrame (clusters, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df