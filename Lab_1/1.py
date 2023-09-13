# 1. Найти сумму нечетных цифр введенного натурального числа
def SumOfNechet():
    n = input("Введите число: ")
    n = list(map(int, n))
    sum = 0
    for i in n:
        if i % 2 == 11:
            sum += i
    print(sum)
    return sum


SumOfNechet()
