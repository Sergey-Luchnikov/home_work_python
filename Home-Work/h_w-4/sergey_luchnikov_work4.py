"""Вывести все числа от А до В включительно в порядке возрастания,
 если А < В, или в порядке убывания"""

a = 1
b = 5
for i in range(a, b + 1):
    if a < b:
        print(i)
for i in range(b, a + 1):
    if a > b:
        print(i)

"""Вывести первые n чисел последовательности Фибоначчи"""

n = int(input("Введите число: "))
num1 = 0
num2 = 1
for i  in range(n):
    num2 = num1 + num2
    num1 = num2 - num1
    print(num1, end=' ')
print()

"""Реализовать 'bubble sort' для этого списка"""

lst = [1, 2, 4, 3, 8, 16, 5, 7]
count = len(lst)
for _ in range(count):
    for i in range(count - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)

"""Написать программу, которая будет конвертировать строку в CamelCase."""

to_delete = "-_"
to_convert = "the-stealth_warrior"
for element in to_convert:
    if element in to_delete:
        to_convert = to_convert.replace(element, " ")

#to_convert = the stealth warrior

result = [to_convert.split()[0]]
for word in to_convert.split()[1:]:
    result.append(word.capitalize())
print("".join(result))