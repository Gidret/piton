N = int(input("N: "))
K = 0 
power_of_3 = 1

while power_of_3 * 3 <= N:
    power_of_3 *= 3
    K += 1

print("Наибольшее число K: ", K)