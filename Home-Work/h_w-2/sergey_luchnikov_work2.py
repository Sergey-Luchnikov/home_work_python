"""Удалить первый и последний символ строки"""

string = input("Введите строку: ")
if len(string) > 2:
      print(string[1:-1])
else:
      print("Error")

"""Настроить отоброжение комментария к отметке 'мне нравится'"""

users = []
if len(users) == 0:
      print("no one likes this")
elif len(users) == 1:
      print(users[0], "likes this")
elif len(users) == 2:
      print(users[0], "and", users[1], "likes this")
elif len(users) == 3:
      print(users[0] + ",", users[1], "and", users[2], "likes this")
else:
      print(users[0] + ",", users[1], "and else", len(users) - 2, "likes this")

"""Есть два списка. Нужно вывести все элементы первого списка, которых нет во втором"""

lst = [1, 2, 3, "hello", "good", "name", 4, 5.3, 6.15, 7.42]
lst1 = [6, 2, 3, "good", "name", "gold", 5.3, 7.42, 8, 9.21]
result = []
for i in lst:
      if i not in lst1:
            result.append(i)
print(result)

"""Создать простой калькулятор, который считывает из строки ввода"""

a = input("Введите значения: ")
s = a.split()
if s[1] == '+':
      print(int(s[0]) + int(s[2]))
elif s[1] == '-':
      print(int(s[0]) - int(s[2]))
elif s[1] == '*':
      print(int(s[0]) * int(s[2]))
elif s[1] == '/':
      print(int(s[0]) / int(s[2]))
else:
      print('Error')

"""Составить список и кортеж из введенных чисел, разделенных запятой"""

a = input("Введите числа: ")
b = a.split(', ')
print(b)
print(tuple(b))

