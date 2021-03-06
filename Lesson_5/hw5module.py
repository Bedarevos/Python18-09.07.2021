def genrefunction(genre):
    """
    Функция принимает на ввод жанр и вытягивает из словаря значение ключей, которые соответствует данному жанру,
    а после добавляет значения ключей в список
    :param genre:
    :return:
    """
    shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
             'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
             'Карточный домик': 'драма',
             'Рик и Морти': 'фантастика'}
    genrelist = set() # Создаем пустое множество, для хранения в нем уникальных элементов
    for i in shows.values(): # Формируем множество с уникальными жанрами, которые есть у нас в словаре в значениях
        genrelist.add(i)

    answer = [] #Создаем пустой список, куда будем добавлять ключи, которые соответсвуют нужному нам жанру
    if genre.lower() in genrelist: #Проверяем есть ли такой жанр в нашем множестве
        for k, v in shows.items(): #Перебираем ключи и значения в нашем словаре
            if v == genre: # Если значение в словаре соответствует нужному жанру
                answer.append(k) #То добавляет ключ, который соответсвует жанру в список
        return answer #после итерации возвращает полный список
    else:
        print("Нет такого жанра в списке")


def ratingfunction(userinput):
    """
    Функция принимает на ввод название шоу и вытягивает из словаря значение рейтинга для данного шоу, который
     соответствует данному жанру, добавляет значения ключей в список, расчитывает среднее число среди значений.
    :param userinput:
    :return:
    """
    ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
               'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

    average = []  # Создаем пустой список для записи рейтинга нужных нам сериалов
    for elem in userinput:
        for key, value in ratings.items():  # Ищем ключ и значение в словаре с жанром
            while key == elem:  # Вычленяем сериалы с нужным нам жанром
                ratelist = ratings[key]  # Вычленяем рейтинг отобранных сериалов по жанрам
                average.append(ratelist)  # Добавляем рейтинг в созданный список
                break

        # Делим сумму на количество для отображения среднего рейтинга
    print("Средний рейтинг для выбранных Вами сериалов составил: ", sum(average) / len(average))
