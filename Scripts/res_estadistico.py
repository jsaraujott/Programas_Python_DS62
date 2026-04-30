# Programa que genera un resumen estadistico de un conjunto de datos
# Me interesa que calcule la media, la desviacion estandar, el cuartil 1, la mediana y el cuartil 3

import pandas as pd
import numpy as np
import argparse

# Generador sintactico
parser = argparse.ArgumentParser()
parser.add_argument("file", type = str)

args = parser.parse_args()

# Programa

datos = pd.read_csv(args.file, header = None)

media = np.mean(datos)
desv = np.std(datos)
q1 = np.quantile(datos,0.25)
med = np.quantile(datos,0.5)
q3 = np.quantile(datos,0.75)

resumen = pd.DataFrame(dict(
    valores = [media,desv, q1, med, q3]
), index = ["Media","Desv. Estandar", "Cuartil 1", "Mediana", "Cuartil 3"])

print(resumen)