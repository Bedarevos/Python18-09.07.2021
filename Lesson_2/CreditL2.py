# Считаем кредит
name1 = input("Введите имя первого человека: ")
name2 = input("Введите имя второго человека: ")

salary1 = int(input("зп первого: "))
salary2 = int(input("зп второго: "))

credit = int(input("Введите сумму кредита: "))
period = int(input("Введите срок в месяцах: "))
procent = float(input("процент: "))

pay_per_month = credit / period + (credit / 100 * procent) / 12
print("Ежемесячный платеж составит - ", pay_per_month, "рублей")