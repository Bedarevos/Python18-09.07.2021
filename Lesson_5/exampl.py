def genrefunction():
    shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
             'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
             'Карточный домик': 'драма',
             'Рик и Морти': 'фантастика'}
    genrelist = set()
    for i in shows.values():
        genrelist.add(i)

    genre = input("Введите жанр: ")


    answer = []
    if genre.lower() in genrelist:
        for k, v in shows.items():
            if v == genre:
               answer.append(k)
        return (answer)
    else:
        print("Нет такого жанра в списке")



def ratingfunction(userinput):
    ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
               'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

    showlist = []
    average = []  # Создаем пустой список для записи рейтинга нужных нам сериалов
    for i in userinput:
        for elem in showlist:
            for key, value in ratings.items():  # Ищем ключ и значение в словаре с жанром
                while key == elem:  # Вычленяем сериалы с нужным нам жанром
                    ratelist = ratings[key]  # Вычленяем рейтинг отобранных сериалов по жанрам
                    average.append(ratelist)  # Добавляем рейтинг в созданный список
                    break

        # Делим сумму на количество для отображения среднего рейтинга
    print("Средний рейтинг для выбранных Вами сериалов составил: ", sum(average) / len(average))

ratingfunction(userinput=genrefunction())
