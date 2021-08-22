def unpacklines(filename):
    file = open(filename)
    content = file.readlines()
    file.close()
    return content


def printing(meaning, objectname):
    for i in objectname:
        if meaning.lower() in i:
            print(i)

with open("lesson05_cats_of_ulthar.txt",) as f:
    count = f.read().count('кошка')
if count:
    print(f'Количество элементов в файле: {count}')
else:
    print('Элементов в файле нет')


printing("кошка", unpacklines("lesson05_cats_of_ulthar.txt"))
