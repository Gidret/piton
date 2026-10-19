n = int(input("Введите трехзначное число: "))

sotnya = n // 100
desyatki = (n // 10) % 10
edinitsy = n % 10

digit_sum = sotnya + desyatki + edinitsy
digit_prod = sotnya * desyatki * edinitsy

print(f"Сумма цифр: {digit_sum}")
print(f"Произведение цифр: {digit_prod}")