# 4.	Отсортируйте словарь по значению в порядке возрастания и убывания.

my_dict = {"a": 3, "b": 1, "c": 2, "d": 5, "e": 4}

sorted_A = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_D = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Сортировка по возрастанию:")
print(sorted_A)

print("\nСортировка по убыванию:")
print(sorted_D)
