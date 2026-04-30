
import argparse

parser = argparse.ArgumentParser(description = "Este es un programa que deterina si un número es primo o compuesto")
parser.add_argument("n", type = int, help = "Numero entero positivo (>0 y sin decimales)")
args = parser.parse_args()

n = args.n

if n <= 0:
    print("Ingrese un numero entero positivo")
else:
    es_primo = True
    if n <= 2:
        es_primo = True
    divisores = []
    for i in range(2,n): #Cito a Euler
        if n % i == 0:
            es_primo = False
            divisores.append(i)

    if es_primo:
        print("Es primo")
    else:
        print("Es compuesto")
        print(f"{divisores[0]} * {int(n / divisores[0])}")