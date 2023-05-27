"""Напишите функцию,
которая принимает на вход список слов и возвращает новый список,
содержащий только те слова, которые состоят только из букв
(верхнего или нижнего регистра)."""

a = ["aple", "Anton", "Bob", "DRIVE", "hello"]

def lst(array):
    new_lst = []
    for i in array:
        if i == i.upper() or i == i.lower():
            new_lst.append(i)
    return new_lst
print(lst(a))

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in b:
    i *= 2
    print(i)