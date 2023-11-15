# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open("./Lab_3/4/File.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

profits = {}
total_profit = 0

for line in lines:
    parts = line.strip().split()
    if len(parts) == 4:
        name, owner, income, expenses = parts
        income = int(income)
        expenses = int(expenses)
        profit = income - expenses

        if profit >= 0:
            profits[name] = profit
            total_profit += profit


average_profit = total_profit / len(profits) if len(profits) > 0 else 0

data_list = [profits, {"average_profit": average_profit}]

with open("./Lab_3/4/firms.json", "w") as json_file:
    json.dump(data_list, json_file)

print("JSON-объект:")
print(data_list)
