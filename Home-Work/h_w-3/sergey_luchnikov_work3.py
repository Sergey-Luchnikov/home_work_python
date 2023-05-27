"""Найти самое большое и самое маленькое число и вернуть их в виде кортежа"""

line = "1 2 3 4 5"
lst = line.split()
print(tuple(min(lst)) + tuple(max(lst)))

"""Из любого целого числа, нужно вернуть новое, максимально возможное число"""

num = input("Введите число: ")
lst = list(num)
lst.sort(reverse=True)
print(int(''.join(map(str, lst))))

"""Нужно вернуть список только из цифр"""

lst = [1, 2, 3, "hello", "world", 4, 5]
result = []
for i in lst:
    if type(i) == int:
        result.append(i)
print(result)

"""Из введенного числа, нужно вывести максимальную цифру"""

num = input("Введите число: ")
num.split()
print(int(max(num)))

