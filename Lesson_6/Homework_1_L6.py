shows = {'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9}, 'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
         'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'}, '24': {'Genre': 'драма', 'Rating': 0.75},
         'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98},
         'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
         'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87}, 'Карточный домик': {'Genre': 'драма', 'Rating': 0.82},
         'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}}

average = 0
count = 0
for i in shows:
    try:
        rating = (shows[i]['Рейтинг'])
        average += rating
        count += 1
    except TypeError:
        print("У шоу ", i, "рейтинг имеет не числовое значение. Данное шоу не включено в расчет")
    except KeyError:
        print("У шоу ", i, "в словаре нет ключа 'Рейтинг'. Данное шоу не включено в расчет")
print("Средний рейтинг всех шоу: ", average / count)
