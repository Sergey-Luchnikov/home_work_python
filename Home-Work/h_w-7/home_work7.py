"""Напишите функцию,
которая принимает строку и возвращает список всех уникальных символов в этой строке."""

str = ["hello world"]

def lst_unique(str):
    unique_symbol = []
    for i in str:
        for j in i:
            if j not in unique_symbol:
                unique_symbol.append(j)
    return ' '.join(unique_symbol).split()
print(lst_unique(str))

""" Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
содержащий только те строки, которые начинаются с буквы 'a' (большой или малой)."""

def lst_str(array):
    lst_a = []
    for i in array:
        if i[0] == "a" or i[0] == "A":
            lst_a.append(i)
    return lst_a
print(lst_str(["aple", "Anton", "Bob", "hello"]))

"""Напишите функцию, которая принимает на вход список чисел и возвращает новый список, 
содержащий только те числа, которые больше среднего значения всех чисел в списке."""

def lst_num(array):
    new_lst_num = []
    average_value = sum(array) / len(array)
    for i in array:
        if i > average_value:
            new_lst_num.append(i)
    return new_lst_num
print(lst_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

"""Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
содержащий те же строки, 
но с замененным первым символом на символ '*' (например, "hello" станет "*ello")."""

def lst_str(array):
    new_lst_str = []
    for i in array:
        a = i.replace(i[0], "*")
        new_lst_str.append(a)
    return new_lst_str
print(lst_str(["name", "lastname", "city", "adres"]))

"""Напишите функцию, которая принимает на вход список списков чисел и возвращает новый список, 
содержащий те же числа, но увеличенные на 1."""

def lst_num_lst(array):
    new_lst_numbers = []
    for i in array:
        new_lst_numbers += i
    new_lst_numbers_1 = []
    for j in new_lst_numbers:
        new_lst_numbers_1.append(j + 1)
    return new_lst_numbers_1
print(lst_num_lst([[1, 8, 12], [5, 34, 6], [41, 22, 123]]))