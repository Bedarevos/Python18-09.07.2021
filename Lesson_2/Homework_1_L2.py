# Приветствуем пользователя

name = input("Добро пожаловать в наше казино, введите, пожалуйста, Ваше имя: ")
print("Добрый день, ", name, ", Вам предоставлен депозит на сумму 10 000 единиц и я предлагаю сыграть со мной в игру:")
print("Я загадываю целое число от 2 до 12 включительно, если Вы угадываете - выигрываете 1000 единиц,")
print("не угадываете - проигрываете 1000. Идет?")


# Задаем переменную, которая отвечает за решение пользователя
des = input("Введите Да или Нет: ")
# Задаем депозит
dep = 10000
# Задаем переменную к журналу
journal = []

# Цикл повторяется, пока не будет ответов Да или Нет
while des != 'Да' or 'Нет':
# Если да, то начинапется игра
    if des == 'Да':
# Начинается игра
# Вводим рандом
        import random
# Задаем диапазон рандома
        a = random.randint(2, 12)
# пользователь вводит свою ставку
        b = int(input("Я загадал число от 2 до 12, теперь загадайте Вы: "))
# Проверям ставку на диапазон, который нам нужен
        while b>12 or b<2:
# Просим пользователя ввести нужную цифру из правильного диапазона
            b = int(input("Загадайте число от 2 до 12 включительно: "))
        else:
# Проверяем депозит на то, что он не нулевой для продолжения игры
            while dep > 0:
# Проверяем угадал ли пользователь ставку
              if a == b:
                dep = dep + 1000
                print("Вы выиграли, я загадал число", a , ", Вы тоже загадали число ", b,". Ваш депозит составляет: ", dep )
# Записываем в журнал ставку
                zapis = "Игра загадала: ", a , ", моя попытка: ", b , " на счету: ", dep
                journal.append(zapis)
# Продолжаем игру для следующей ставки
                b = int(input("Загадайте новое число от 2 до 12 "))
                while b > 12 or b < 2:
                    b = int(input("Загадайте число от 2 до 12 включительно: "))
                a = random.randint(2, 12)
              else:
                dep = dep - 1000
                print("Очень жаль, я загадал число", a, ", Вы загадали число", b, ". Ваш депозит составляет: ", dep)
                zapis = "Игра загадала: ", a,  ", моя попытка: ", b,  " на счету: ", dep
                journal.append(zapis)
                if dep == 0:
# Прекращаем игру, так как депозит пуст
                    print("К сожалению Ваш депозит пуст, Вы проиграли")
# Печатаем журнал
                    for record in journal:
                        print(record)
                    break
                b = int(input("Загадайте новое число от 2 до 12: "))
                while b > 12 or b < 2:
                    b = int(input("Загадайте число от 2 до 12 включительно: "))
                a = random.randint(2, 12)
            break

# Если нет, то все заканчивается
    elif des == 'Нет':
        print("Мне очень жаль, приходите, когда захотите поиграть")
        break
# Если ни да, ни нет, то цикл повторяется
    else: des= input("Введите Да или Нет c большой буквы: ")