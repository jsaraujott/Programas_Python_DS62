import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description = "Programa que grafica un histograma Normal dadas unas medidas de localizacion y escala") 
parser.add_argument("media", type = float, help = "Medida de localización del histograma")
parser.add_argument("desv", type = float, help = "Medida de escala del histograma")
parser.add_argument("-N","--n", default = 100, type = int, help = "Tamaño de muestra")

args = parser.parse_args()

datos = np.random.normal(size = args.n, loc = args.media, scale = args.desv)
datos = datos.round(0).astype(int)

datos_trim = []
for i in range(len(datos)):
    if datos[i] <= abs(args.media) + 3*args.desv or datos[i] >= abs(args.media) - 3*args.desv:
        datos_trim.append(datos[i])
datos_trim = pd.DataFrame(datos_trim)
datos_trim.columns = ['Datos']

histograma = datos_trim.groupby('Datos').size()
for i in range(len(histograma)):
    if histograma.index[i]>=0:
        s = "+"
    else:
        s = ""
    print(
        s,
        histograma.index[i],
        ' '*(1+len(str(np.max([np.max(histograma.index),
                               abs(np.min(histograma.index))]))) - 
                               len(str(abs(histograma.index[i])))),
        '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
        sep = ""
    )