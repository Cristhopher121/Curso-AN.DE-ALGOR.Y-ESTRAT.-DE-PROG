import math
import random

# Ingreso de datos
a = float(input("Ingrese el valor de a (elipse): "))
b = float(input("Ingrese el valor de b (elipse): "))
c = float(input("Ingrese el valor de c (hipérbola): "))
d = float(input("Ingrese el valor de d (hipérbola): "))
cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))

# Validación
if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cantidad <= 0:
    print("Error: todos los valores deben ser positivos.")
    exit()

# Contadores
puntos_elipse = 0
puntos_interseccion = 0

# Generación de puntos aleatorios: x entre -a y a, y entre -b y b
for _ in range(cantidad):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)

    # ¿Cae dentro de la elipse?  x²/a² + y²/b² <= 1
    if (x**2) / (a**2) + (y**2) / (b**2) <= 1:
        puntos_elipse += 1

        # ¿Cae también dentro de la hipérbola?  x²/c² - y²/d² >= 1
        if (x**2) / (c**2) - (y**2) / (d**2) >= 1:
            puntos_interseccion += 1

# Área de la elipse por fórmula
area_elipse = math.pi * a * b

# Área de la intersección por proporción respecto a la elipse
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