# Создать классы: «Книга», «Отдел», «Библиотека». В классах реализовать
# следующие методы: добавление, удаление, изменение названия книг из
# отделов. Классы должны содержать методы доступа и изменения всех полей.
# Предусмотреть метод записи информации в файл


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Жанр: {self.genre}"

    def change_title(self, new_title):
        self.title = new_title


class Department:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Нет такой книги")

    def change_book_title(self, book, new_title):
        for b in self.books:
            if b == book:
                b.change_title(new_title)


class Library:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def remove_department(self, dep):
        if dep in self.departments:
            self.departments.remove(dep)

    def write_info_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for dep in self.departments:
                file.write(f"Отдел: {dep.name}\n")
                for book in dep.books:
                    file.write(book.get_info() + "\n")


library = Library()
while True:
    print("\nМеню:")
    print("1. Добавить отдел")
    print("2. Удалить отдел")
    print("3. Добавить книгу в отдел")
    print("4. Удалить книгу из отдела")
    print("5. Изменить название книги")
    print("6. Записать информацию в файл")
    print("7. Просмотреть Отделы и Книги в них")
    print("8. Выйти из программы")

    choice = input("Выберите действие (1-7): ")

    if choice == "1":
        dep_name = input("Введите название нового отдела: ")
        dep = Department(dep_name)
        library.add_department(dep)
        print(f"Отдел '{dep_name}' добавлен.")
    elif choice == "2":
        dep_name = input("Введите название отдела для удаления: ")
        for dep in library.departments:
            if dep.name == dep_name:
                library.remove_department(dep)
                print(f"Отдел '{dep_name}' удален.")
                break
        else:
            print(f"Отдел '{dep_name}' не найден.")
    elif choice == "3":
        dep_name = input("Введите название отдела для добавления книги: ")
        book_title = input("Введите название книги: ")
        book_author = input("Введите автора книги: ")
        book_genre = input("Введите жанр книги: ")
        for dep in library.departments:
            if dep.name == dep_name:
                book = Book(book_title, book_author, book_genre)
                dep.add_book(book)
                print(f"Книга '{book_title}' добавлена в отдел '{dep_name}'.")
                break
        else:
            print(f"Отдел '{dep_name}' не найден.")
    elif choice == "4":
        dep_name = input("Введите название отдела для удаления книги: ")
        book_title = input("Введите название книги: ")
        for dep in library.departments:
            if dep.name == dep_name:
                for book in dep.books:
                    if book.title == book_title:
                        dep.remove_book(book)
                        print(f"Книга '{book_title}' удалена из отдела '{dep_name}'.")
                        break
                else:
                    print(f"Книга '{book_title}' не найдена в отделе '{dep_name}'.")
                break
        else:
            print(f"Отдел '{dep_name}' не найден.")
    elif choice == "5":
        dep_name = input("Введите название отдела для изменения названия книги: ")
        book_title = input("Введите название книги: ")
        new_title = input("Введите новое название для книги: ")
        for dep in library.departments:
            if dep.name == dep_name:
                for book in dep.books:
                    if book.title == book_title:
                        dep.change_book_title(book, new_title)
                        print(
                            f"Название книги изменено на '{new_title}' в отделе '{dep_name}'."
                        )
                        break
                else:
                    print(f"Книга '{book_title}' не найдена в отделе '{dep_name}'.")
                break
        else:
            print(f"Отдел '{dep_name}' не найден.")
    elif choice == "6":
        library.write_info_to_file("./Lab_4/3/library.txt")
        print(f"Информация записана в файл 'library.txt'.")
    elif choice == "7":
        for dep in library.departments:
            print(f"Отдел: {dep.name}")
            for book in dep.books:
                print("\t" + book.get_info())
    elif choice == "8":
        break
    else:
        print("Неверный выбор")
