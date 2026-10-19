A = int(input("A: "))
B = int(input("B: "))

product = 1
for i in range(A, B + 1):
    product *= i

print("Произведение:", product)