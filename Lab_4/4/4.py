# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические методы, методы класса.


class Student:
    university = "БГУИР"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Студент: {self.name}, Возраст: {self.age}, Средний балл: {self.grade}"

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

    def set_grade(self, new_grade):
        self.grade = new_grade

    def get_grade(self):
        return self.grade


student1 = Student("Иван", 20, 4.5)
student2 = Student("Мария", 19, 4.2)

Student.change_university("Новый университет")

student2.set_grade(4.7)

print(student1.get_info())
print(student2.get_info())

print(f"Студент 1 совершеннолетний: {Student.is_adult(student1.age)}")
print(f"Студент 2 совершеннолетний: {Student.is_adult(student2.age)}")
