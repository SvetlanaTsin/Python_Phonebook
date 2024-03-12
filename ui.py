from logger import input_data, print_data, change_data, delete_data


def interface():
    print('Добрый день! Вас приветствует бот-справочник от Geekbrains! \n 1 - записать данные \n 2 - вывести данные \n 3 - изменить данные \n 4 - удалить данные')
    command = int(input('Введите число: '))  #в эту переменную будем принимать команды от пользователя из консоли

    while command not in [1, 2, 3, 4]: #если польз вводит неверное число
        print('Неправильный ввод')
        command = int(input('Введите число: '))

    if command == 1:
        input_data() 
    elif command == 2:
        print_data() 
    elif command == 3:
        change_data() 
    elif command == 4:
        delete_data()