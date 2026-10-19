A = int(input("A: "))
B = int(input("B: "))

sum_sq = 0
for i in range(A, B + 1):
    sum_sq += i ** 2

print("Сумма квадратов:", sum_sq)