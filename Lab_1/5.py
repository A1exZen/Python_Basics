import os

products = {
    "торт": ["Морковный торт", 150, 2500],
    "пирожное": ["Шоколадное пирожное", 50, 500],
    "кофе": ["Латте", 80, 1000],
    "пончик": ["Пышный пончик", 60, 500],
    "эклер": ["Ванильный эклер", 70, 500],
    "печенье": ["Арахисовое печенье", 30, 1500],
}


def show_description():
    os.system("CLS")
    for product, info in products.items():
        print(f"{product} - {info[0]}")


def show_price():
    os.system("CLS")
    for product, info in products.items():
        print(f"{product} - {info[1]} руб. за 100гр")


def show_quantity():
    os.system("CLS")
    for product, info in products.items():
        print(f"{product} - {info[2]} гр")


def show_all_info():
    os.system("CLS")
    for product, info in products.items():
        print(f"{product}:")
        print(f"Описание: {info[0]}")
        print(f"Цена: {info[1]} грн за 100гр")
        print(f"Количество: {info[2]} гр\n")


def purchase(my_money):
    os.system("CLS")
    total_cost = 0
    while True:
        product = input(
            "Введите название продукта (exit - завершить покупку): "
        ).lower()
        if product == "exit":
            break
        if product in products:
            quantity = int(input(f"Введите кол-во {product} (в граммах): "))
            if quantity > products[product][2]:
                print(f"Извините, недостаточно {product} в наличии.")
            else:
                cost = (quantity / 100) * products[product][1]

                total_cost += cost
                if my_money < total_cost:
                    print("Недостаточно средств для покупки")
                    total_cost -= cost
                    return
                products[product][2] -= quantity
                print(f"{quantity} гр {product} добавлено в корзину.")
        else:
            print("Такого продукта нет в меню. Попробуйте еще раз.")
    print(f"Итого к оплате: {total_cost} руб.")
    ch = input("Оплатить покупку? (y/n)")
    if ch == "y":
        my_money -= total_cost
        return my_money
    elif ch != "n":
        print("Ошибка")
        return


my_money = int(input("Введите ваш баланс: "))
while True:
    print(f"\nВаш баланс:{my_money}")
    print("Меню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        show_description()
    elif choice == "2":
        show_price()
    elif choice == "3":
        show_quantity()
    elif choice == "4":
        show_all_info()
    elif choice == "5":
        my_money = purchase(my_money)
    elif choice == "6":
        print("Покупка завершена!")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
