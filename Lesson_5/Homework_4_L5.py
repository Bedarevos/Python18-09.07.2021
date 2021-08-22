def diaryadd():
    with open("diary.txt", "a") as file:
        data = input("Введите сегодняшнюю дату: ")
        message = input("Введите сообщение, которое хотите занести в дневник: ")
        file.write(data)
        file.write(": ")
        file.write(message)
        file.write("\n")
        print("Ваше сообщение добавлено в дневник")


diaryadd()



