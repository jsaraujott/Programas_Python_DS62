# Este programa imprime los 5 primeros numeros pares
import argparse

# Crear un generador sintactico de variables (parser)
parser = argparse.ArgumentParser()
parser.add_argument("numero", type = int)

# Guardar las variables del parser en un objeto de python
args = parser.parse_args()

n = int(args.numero)

for i in range(1,n*2 + 1):
    if i % 2 == 0:
        print(i)