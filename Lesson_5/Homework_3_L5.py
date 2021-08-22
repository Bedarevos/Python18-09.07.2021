def unpacklines(filename): #Вводим функцию, которая открывает файл
    """
    Функция открывает для чтения текстовый файл в режиме многострочности и возвращает его содержимое
    :param filename:
    :return:
    """
    file = open(filename)
    content = file.readlines() #Открываем в режиме многострочности, чтобы работать отдельно с каждой строкой
    file.close()
    return content


def printing(meaning, objectname): #Вводим функцию, которая ищет значение meaning
    """
    Функция ищет значение meaning в параметре objectname и если данное значение есть в данном параметре, распечатывает параметр
    :param meaning:
    :param objectname:
    :return:
    """
    for i in objectname:
        if meaning.lower() in i:
            print(i)


with open("lesson05_cats_of_ulthar.txt",) as f: #Мне такой вариант открытия файлов показался проще, подсмотрел в гугле
    count = f.read().count('кошка') #Считаю во всем тексте слово кошка
if count:
    print(f'Количество элементов в файле: {count}')
else:
    print('Элементов в файле нет')


printing("кошка", unpacklines("lesson05_cats_of_ulthar.txt")) #Вызываю функцию распечатывания строк в которой функция открытия файла
