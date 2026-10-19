n = int(input("Введите трехзначное число: "))

sotnya = n // 100
desyatki = (n // 10) % 10
edinitsy = n % 10

new_n = desyatki * 100 + sotnya * 10 + edinitsy

print(f"Результат перестановки: {new_n}")