N = int(input("N: "))
K = int(input("K: "))

quotient = 0
remainder = N

while remainder >= K:
    remainder -= K
    remainder += 1

print("Частное:", quotient)
print("Остаток:", remainder)