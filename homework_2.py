import math
# Задача 1. Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.

# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def list_of_factorial():
    n = int(input("Enter number N: "))
    list = []
    if n > 0:
        for i in range(1, n+1):
            list.append(math.factorial(i))
    else:
        print("Enter N more than 0")
    print(list, end=' ')

list_of_factorial()
print()
# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def table():
    print("X | Y | Z | ¬(X ∧ Y) ∨ Z")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"{x} | {y} | {z} | {int((not(x and y) or z))}")

table()

# Задача 3. Даны две строки. 
# Посчитайте сколько раз каждый символ первой строки встречается во второй

# «one» «onetwonine» - o – 2, n – 3, e – 2

def strokes():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    for i in range(len(s1)):
        print(f"{s1[i]} - {s2.count(s1[i])}")

strokes()

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

# 3 -> [2, 3, -3, -2, -1, 0, 1]

def list_shift():
    n = int(input("Enter N: "))
    r = range(-n, n + 1)
    list = []
    for i in r:
        list.append(i)
    print(list)
    list = list[-2:] + list[:-2]
    print(list)

list_shift()