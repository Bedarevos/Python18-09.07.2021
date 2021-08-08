shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма', 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98, 'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

import random
movielist = [] # Создаем пустой список чтобы записывать в него названия сериалов
for elem in shows.keys(): # Вычленяем только названия сериалов в список
    movielist.append(elem)

programmchoice = random.choice(movielist) # Выбираем фильм из списка
genre = shows[programmchoice]
rate = ratings[programmchoice]
while genre == "фэнтази" or rate < 0.85:
    programmchoice = random.choice(movielist)  # Выбираем фильм из списка
    genre = shows[programmchoice]
    rate = ratings[programmchoice]
    continue
    while genre != "фэнтази" and rate >= 0.85:
        print(programmchoice)
        userchoice = input("Вас устраивает данное шоу?")
        if userchoice.lower() == "да":
            print ("Приятного просмотра")
            break
        elif userchoice.lower() == "нет":
            programmchoice = random.choice(movielist)  # Выбираем фильм из списка
            genre = shows[programmchoice]
            rate = ratings[programmchoice]
            print(programmchoice)
            userchoice = input("Вас устраивает данное шоу?")
            continue
            if userchoice.lower() == "да":
                print("Приятного просмотра")
                break
            else:
                input("Введита да или нет")
# elif:
#     programmchoice = random.choice(movielist)  # Выбираем фильм из списка
#     genre = shows[programmchoice]
#     rate = ratings[programmchoice]
