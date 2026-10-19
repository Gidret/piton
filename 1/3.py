import math

pi = 3.14

S = float(input("Введите площадь круга S: "))

R = math.sqrt(S / pi)
D = 2 * R
L = 2 * pi * R

print(f"Диаметр D: {D}")
print(f"Длина окружности L: {L}")