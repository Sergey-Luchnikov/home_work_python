"""Напишите функцию,
которая принимает список чисел и возвращает список квадратов этих чисел."""

def square_numbers(array):
    empty_list = []
    for i in array:
        empty_list.append(i ** 2)
    return empty_list
print(square_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""Напишите функцию, которая принимает на вход список строк и возвращает список строк, 
длина которых больше 5 символов."""

def string_list(array):
    new_lst = []
    for i in array:
        if len(i) > 5:
            new_lst.append(i)
    return new_lst
print(string_list(["hello", "baracuda", "garage", "name", "lastname"]))

"""Напишите функцию, 
которая принимает на вход список чисел и возвращает только четные числа из этого списка."""

def numbers_list(array):
    new_numbers_list = []
    for i in array:
        if i % 2 == 0:
            new_numbers_list.append(i)
    return new_numbers_list
print(numbers_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""Напишите функцию, которая принимает на вход список чисел и 
возвращает сумму квадратов четных чисел из этого списка. """

def num_list(array):
    new_num_list = []
    for i in array:
        if i % 2 == 0:
            new_num_list.append(i ** 2)
    return new_num_list
print(num_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""Напишите функцию, которая принимает на вход список строк и 
возвращает список строк, которые начинаются с буквы "a". """

def str_list(array):
    new_str_list = []
    for i in array:
        if i[0] == "a" or i[0] == "A":
            new_str_list.append(i)
    return new_str_list
print(str_list(["Alisa", "aple", "black", "green"]))

"""Напишите функцию, которая принимает на вход список чисел и возвращает список чисел, 
которые больше 10 и меньше 20."""

def list_num(array):
    new_list = []
    for i in array:
        if i > 10 and i < 20:
            new_list.append(i)
    return new_list
print(list_num([1, 2, 12, 14, 16, 19, 20, 24]))

"""Напишите функцию, которая принимает на вход список строк и возвращает список строк, 
которые содержат букву "e". """

def lst_str(array):
    new_lst = []
    for i in array:
        for j in i:
            if j == "е":
                new_lst.append(i)
    return list(set(new_lst))
print(lst_str(["Привет", "Мир", "Меня", "Зовут", "Сергей"]))

"""Напишите функцию, которая принимает на вход список чисел и возвращает True, 
если все числа в списке положительные, и False в противном случае. """

def lst_numbers(array):
    for i in array:
        if i < 0:
            return False
    return True
print(lst_numbers([1, 2, 3, 4, 5, 6]))
