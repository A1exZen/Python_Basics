# Создать текстовый файл (не программно). Построчно записать названия ювелирных украшений и их стоимость (не менее 10 строк).
# Вывести на экран все украшения дешевле 100 рублей. Найти среднюю стоимость украшений.
# Пример файла:
# Кольцо  120
# Цепочка  800

try:
    with open("./Lab_3/2/File.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
except IOError:
    print("Ошибка!")

arr = []
total_price = 0
for line in lines:
    str = line.split()
    if len(str) == 2:
        name, price = str
        price = float(price)
        total_price += price
        if price <= 100:
            arr.append(str)

print("Украшения дешевле 100 руб: ")
for str in arr:
    name, price = str
    print(f"{name}: {price}")


avarage = total_price / len(lines)
print(f"Средняя стоимость всех украшений: {round(avarage, 2)} ")
