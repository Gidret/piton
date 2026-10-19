N = int(input("N: "))

double_factorial = 1.0
while N > 0:
    double_factorial *= N
    N -= 2

print("Двойной факториал: ", double_factorial)