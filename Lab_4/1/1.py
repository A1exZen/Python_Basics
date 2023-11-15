# Создать класс List (список), в котором реализовать методы для работы со
# списком (не менее 5).


class MyList:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def remove_item(self, item):
        if item in self.data:
            self.data.remove(item)

    def get_length(self):
        return len(self.data)
    
    def get_items(self):
        return self.data
    
    def clear_list(self):
        self.data = []



my_list = MyList()
my_list.add_item(1)
my_list.add_item(2)
my_list.add_item(3)
my_list.add_item(4)
my_list.add_item(5)

print("Список:", my_list.get_items())
print("Длина списка:", my_list.get_length())

my_list.remove_item(2)
print("Список после удаления элемента 2:", my_list.get_items())

my_list.clear_list()
print("Список после очистки:", my_list.get_items())
