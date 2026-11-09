import math
import random


a = float(input("Ingrese el valor de a (elipse): "))
b = float(input("Ingrese el valor de b (elipse): "))
c = float(input("Ingrese el valor de c (hipérbola): "))
d = float(input("Ingrese el valor de d (hipérbola): "))
cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))


if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cantidad <= 0:
    print("Error: todos los valores deben ser positivos.")
    exit()

puntos_elipse = 0
puntos_interseccion = 0

for _ in range(cantidad):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)

    if (x**2) / (a**2) + (y**2) / (b**2) <= 1:
        puntos_elipse += 1

        if (x**2) / (c**2) - (y**2) / (d**2) >= 1:
            puntos_interseccion += 1

# Área de la elipse por fórmula
area_elipse = math.pi * a * b

if puntos_elipse > 0:
    area_interseccion = area_elipse * puntos_interseccion / puntos_elipse
else:
    area_interseccion = 0

# Resultados
print("\n=========== RESULTADOS ===========")
print(f"Puntos generados: {cantidad}")
print(f"Puntos dentro de la elipse: {puntos_elipse}")
print(f"Puntos en la intersección elipse-hipérbola: {puntos_interseccion}")
print(f"\nÁrea de la elipse (fórmula): {area_elipse:.4f}")
print(f"Área aproximada de la intersección: {area_interseccion:.4f}")