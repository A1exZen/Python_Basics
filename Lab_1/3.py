# 3.	Дан список list=[1612,49,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке. Все слова: посчитать количество гласных и согласных. Вывести всё на экран

my_list = [1612, 49, "hello", 6, 19, "world"]

print(f"{my_list}\n")

if isinstance(my_list, list):
    for i in my_list:
        sumD, sogl, glasn = 0, 0, 0
        if isinstance(i, int):
            if i % 2 == 0:
                sumD = sum(int(num) for num in str(i))
                print(f"{i} = {sumD}")
            else:
                i = 1
                print(f"{i}")
        elif isinstance(i, str):
            for ch in i:
                if ch.lower() not in "aeiouy":
                    sogl += 1
                else:
                    glasn += 1
            print(f"{i} = sogl: {sogl}, glasn:{glasn}")
else:
    print("Список не определен")
