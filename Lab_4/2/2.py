# Создать классы «Транспортное средство», «Самолет», «Поезд»,
# «Автомобиль». Определить время и стоимость перевозки для указанных
# городов и расстояний. Вывести данные о наиболее быстрой и экономичной
# поездке. Предусмотреть метод записи информации в файл


class Transport:
    def __init__(self, name, speed, cost_km):
        self.name = name
        self.speed = speed
        self.cost_km = cost_km

    def calc_time(self, distance):
        return distance / self.speed

    def calc_cost(self, distance):
        return distance * self.cost_km


class Airplane(Transport):
    def __init__(self):
        super().__init__("Самолет", 250, 3)


class Train(Transport):
    def __init__(self):
        super().__init__("Поезд", 150, 1)


class Car(Transport):
    def __init__(self):
        super().__init__("Авто", 100, 2)


def write_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


distance = 500
city_a = "Город A"
city_b = "Город B"


airplane = Airplane()
train = Train()
car = Car()

time_airplane = airplane.calc_time(distance)
cost_airplane = airplane.calc_cost(distance)
time_train = train.calc_time(distance)
cost_train = train.calc_cost(distance)
time_car = car.calc_time(distance)
cost_car = car.calc_cost(distance)


fastest_transport = min([airplane, train, car], key=lambda x: x.calc_time(distance))

cheapest_transport = min([airplane, train, car], key=lambda x: x.calc_cost(distance))


print(f"Самое быстрое транспортное средство для перевозки между {city_a} и {city_b}: {fastest_transport.name}")
print(f"Время: {fastest_transport.calc_time(distance):.2f} часов")
print(f"Самое экономичное транспортное средство: {cheapest_transport.name}")
print(f"Стоимость: {cheapest_transport.calc_cost(distance):.2f} рублей")


data_to_write = (
    f"Информация о поездке между {city_a} и {city_b}:\n"
    f"Самое быстрое транспортное средство: {fastest_transport.name}\n"
    f"Время: {fastest_transport.calc_time(distance):.2f} часов\n"
    f"Самое экономичное транспортное средство: {cheapest_transport.name}\n"
    f"Стоимость: {cheapest_transport.calc_cost(distance):.2f} рублей\n"
)

write_to_file("./Lab_4/2/trip.txt", data_to_write)
