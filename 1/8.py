A = int(input("A: "))
B = int(input("B: "))

total_sum = 0
for i in range(A, B + 1):
    total_sum += i

print("Сумма:", total_sum)