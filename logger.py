import csv

from data_create import name_data, surname_data, phone_data, address_data

#ВВОД ДАННЫХ двух разных вариантах (каждые данные сновой строки или все в одну строчку)

def input_data():
    name = name_data()  #создадим функцию name_data для ввода данных, чтобы не писать много раз input. Положим ее в другой модуль
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n \n" # в переменной var предлагаем польз выбрать, в каком формате он хочет записать свои данные, и сохраняем его выбор
                    f"1 вариант: \n"
                      f"{name}\n{surname}\n{phone}\n{address}\n\n"
                      f"2 вариант: \n"
                      f"{name};{surname};{phone};{address}\n"
                      f"Выберите вариант: "))
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='UTF-8') as v1: #при выборе 1-го вар открываем файл с данными 1-го типа, указываем режим записи (а) и кодировку. Открываем файл как v1 (временно даем имя v1)
            v1.write(f"{name}\n{surname}\n{phone}\n{address}\n\n") #даем команду записать в файл вот в таком формате (с новой строки каждые данные)

    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as v2:
            v2.write(f"{name};{surname};{phone};{address}\n\n")


 

#ПЕЧАТЬ ДАННЫХ:
            
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='UTF-8') as v1:
        data_first = v1.readlines()   #в переменную data_first мы кладем все прочитанные строки из файла (хранится в виде списка)
        data_first_list = [] #создаем пустой список, туда будем класть все прочитанные строки
        j = 0
        for i in range(len(data_first)): #проходим по значениям прочтенного списка
            if data_first[i] == '\n' or i == len(data_first) - 1: #пока цикл не дойдет до разделителя \n или до последнего элемента, ничего не записывается
                data_first_list.append(''.join(data_first[j:i + 1])) #когда условие выполнено, записывается все, что было на один элемент до разделителя и сам разделитель; т.о. преобразуем в строку
                j = i

        print(*data_first_list) 

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='UTF-8') as v2:
        data_second = v2.readlines()
        print(*data_second)


        

 #ИЗМЕНЕНИЕ

def change_data():
    var = int(input(f"В каком файле изменить данные?\n"
                    f"1 - в первом файле\n"
                    f"2 - во втором файле\n"
                    f"Выберите вариант: "))
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число: '))

    if var == 1:
         with open("data_first_variant.csv", 'r', encoding='utf-8') as v1:
            data = v1.readlines()
            print("Доступные данные для изменения:")
            print(*data)

            line_number = int(input("Введите номер строки, которую хотите изменить: "))
            while line_number < 1 or line_number > len(data):
                print("Неправильный номер строки")
                line_number = int(input('Введите число: '))

            new_data = input("Введите новые данные: ")

            data[line_number-1] = new_data + " \n"

            with open("data_first_variant.csv", 'w', encoding='utf-8') as v1:
                v1.writelines(data)

    if var == 2:
        with open("data_second_variant.csv", 'r', encoding='utf-8') as v2:
            data = v2.readlines()            

        print("Доступные данные для изменения:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input('Введите число: '))

        new_data = name_data() + "; " + surname_data() + "; " + phone_data() + "; " + address_data()

        data[line_number-1] = new_data + "\n"

        with open("data_second_variant.csv", 'w', encoding='utf-8') as v2:
            v2.writelines(data)



#УДАЛЕНИЕ

def delete_data():
    var = int(input(f"Из какого файла удалить данные?\n"
                    f"1 - из первого файла\n"
                    f"2 - из второго файла\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число: '))

    if var == 1:
        with open("data_first_variant.csv", 'r', encoding='utf-8') as v1:
            data = v1.readlines()
            print("Доступные данные для удаления:")
            print(*data)
        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input('Введите число: '))

        data.pop(line_number-1)
        
        with open("data_first_variant.csv", 'w', encoding='utf-8') as v1:
            v1.writelines(data)
            

    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as v2:
            data = v2.readlines()
            print("Доступные данные для удаления:")
            print(*data)

            line_number = int(input("Введите номер строки, которую хотите удалить: "))
            while line_number < 1 or line_number > len(data):
                print("Неправильный номер строки")
                line_number = int(input('Введите число: '))

            data.pop(line_number-1)

            with open("data_second_variant.csv", 'w', encoding='utf-8') as v2:
                v2.writelines(data)



    