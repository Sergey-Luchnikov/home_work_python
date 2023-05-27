"""Напишите функцию, которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами."""

def sum_range(start, end):
    sum = 0

    if start > end:
        start, end = end, start

    for i in range(start, end + 1):
        sum += i
    return sum
print(sum_range(10, 20))

"""Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром."""

def palindrome(num):
    while str(num) != str(num)[::-1]:
        num += 1
    return num
print(palindrome(23))
