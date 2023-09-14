# Напишите программу, демонстрирующую работу try\except\finally

try:
    # Здесь может возникнуть исключение
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: Введите корректное число!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена.")

