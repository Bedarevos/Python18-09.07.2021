import random
n = int(input("Введите количество участников: "))
win_num = int(input("Введите количество победителей: "))
alredy_win = []
for i in range(1, win_num+1):
    temp = random.randint(1, n)
    while temp in alredy_win:
        temp = random.randint(1, n)
    alredy_win.append(temp)
    print("Победитель номер", i , " -", temp)