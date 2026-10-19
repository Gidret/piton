N = int(input("N: "))

while N > 1 & N % 3 == 0:
    N //= 3

if N == 1:
    print("TRUE")
else:
    print("FALSE")