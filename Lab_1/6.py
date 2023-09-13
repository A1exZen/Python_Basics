# Вывести первый и последний элементы отсортированного кортежа в порядке убывания
my_tuple = (5, 2, 8, 1, 9, 3)

sorted_tuple = tuple(sorted(my_tuple, reverse=True))

print("Первый элемент:", sorted_tuple[0])
print("Последний элемент:", sorted_tuple[-1])
