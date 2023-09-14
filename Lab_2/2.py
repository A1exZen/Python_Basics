# Напишите функцию, которая будет принимать один аргумент. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то сумму после первого отрицательного элемента. Удалить все повторяющиеся элементы.
# Число – кол-во четных цифр.
# Строка – найти сумму всех чисел.
# Сделать проверку со всеми этими случаями.


def type_def(el):
    if isinstance(el, tuple):
        sumW = 0
        for i in range(len(el)):
            if isinstance(el[i], str):
                print(f'{i}: {len(el[i])}')

    elif isinstance(el, list):
        my_sum = 0
        nagative = False
        for i in el:
            if isinstance(i, int):
                if i < 0 and not nagative:
                    nagative = True
                    continue
                if nagative:
                    my_sum += i
        el = list(set(el))
        return el, my_sum

    elif isinstance(el, int):
        chet = 0
        for i in str(el):
            i = int(i)
            if i % 2 == 0:
                chet += 1
        return chet

    elif isinstance(el, str):
        nums = sum(int(s) for s in list(el) if s.isdigit())
        return nums


data = ("apple", "banana", "cherry")
result = type_def(data)

data = [-1, 2, 3, -4, 5, -1]
result = type_def(data)
print(result)

data = 2468642
result = type_def(data)
print(result)

data = "Hello 10 ekk12ke1"
result = type_def(data)
print(result)
