# 1. Создать программный файл F1 в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2 все строки, которые содержат только одно слово. Найти самое длинное слово в  файле F2.

import os

with open("./Lab_3/1/F1.txt", "w") as F1:
    while True:
        u_input = input("Введите строку: ")
        if not u_input:
            break
        F1.write(u_input + "\n")

os.system("CLS")

with open("./Lab_3/1/F1.txt", "r") as F1, open("./Lab_3/1/F2.txt", "w") as F2:
    for line in F1:
        words = line.split()
        if len(words) == 1:
            F2.write(line)


with open("./Lab_3/1/F2.txt", "r") as F2:
    lines = F2.readlines()
    if lines:
        longest = max(lines, key=len)
        print(f"Самое длинное слово в F2.txt: {longest}")
    else:
        print("Пустой файл")
