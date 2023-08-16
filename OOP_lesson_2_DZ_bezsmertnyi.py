#LESSON 2 PRACTICE + LESSON 3

# Створити клас Employee.
# __init__ має приймати наступні аргументи: ім’я, ЗП за один робочий день.
# Створити метод work(self, …) який повертає строку “I come to the office.”
# Створити класи Recruiter та Developer, які наслідують клас Employee.
# Перевизначити методи work в класах R та D, щоб вони повертали значення:
# “I come to the office and start to coding.” - для Developer
# “I come to the office and start to hiring.” - для Recruiter
# Перевизначити методи __str__, щоб они повертали строку: “Посада: Ім’я”
# Зробити можливим порівнювати Employee по рівню ЗП.
# +++++++++++++++++++++++++
#Створити метод check_salary(self, days), який розраховує ЗП за передану кількість днів.
#** Зробити можливим, щоб метод check_salary рахував ЗП з початку місяця до поточного дня, не враховуючи вихідні дні.
#Додати в конструктор класу Developer атрибут tech_stack (список з назвами технологій).
#Для класу Developer зробити порівняння за кількістю технологій.
#Зробити можливим операцію додавання об’єктів класу Developer. Результатом має бути новий об’єкт, в якому name = name1 + ‘ ’ + name2, 
#a tech_stack - список з технологій двох об’єктів (тільки унікальні #значення), ЗП - більша з двох.

import datetime

class Employee:
    def __init__(self, name, day_salary):
        self.name = name
        self.day_salary = day_salary

    def work(self):
        return "I come to the office."

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __gt__(self, other):
        return self.day_salary > other.day_salary

    def check_salary(self, days=None):
        if days is None:
            today = datetime.date.today()
            days = today.day

        work_days = 0
        current_date = datetime.date.today()
        for day in range(1, days + 1):
            if current_date.replace(day=day).weekday() < 5:
                work_days += 1

        return self.day_salary * work_days

class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."


class Developer(Employee):
    def __init__(self, name, day_salary, tech_stack):
        super().__init__(name, day_salary)
        self.tech_stack = tech_stack
    def work(self):
        return "I come to the office and start to coding."

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __add__(self, other):
        added_name = self.name + ' ' + other.name
        added_tech_stack = list(set(self.tech_stack + other.tech_stack))
        added_salary = max(self.day_salary, other.day_salary)

        return Developer(added_name, added_salary, added_tech_stack)

Employee1 = Employee("Denys", 999)
Employee2 = Recruiter("Mark", 550)
Employee3 = Developer("Sofia", 720, ["Python", "JavaScript", "HTML", "CSS"])
Employee4 = Developer("John", 800, ["Java", "C#", "C++"])

print(Employee1.work(), '\n', Employee2.work(), '\n', Employee3.work(), sep='')

print(Employee1, '\n', Employee2, '\n', Employee3, sep='')

print(Employee1 > Employee4, '\n', Employee2 > Employee3, sep='')

print(Employee1.check_salary())

print(Employee3>Employee4)

combined_developer = Employee3 + Employee4

print(combined_developer.name)
print(combined_developer.tech_stack)
print(combined_developer.day_salary)

#LESSON 2 HOMEWORK
CURRENT = 2023
class Human:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def to_str(self):
        return f'Person: {self.name} and birth {self.birth_date}'

    def __str__(self):
        return self.to_str()

    def get_age(self):
        return CURRENT - self.birth_date

    def __eq__(self, other):
        return self.name == other.name and self.birth_date == other.birth_date

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f"Creating an instance of {cls.__name__}")
        return instance

class Planet:

    def __init__(self, name):
        self.name = name
        self.humans = []

    def to_str(self):
        return f'Planet called: {self.name}'

    def __str__(self):
        return self.to_str()

    def add_human(self, human):
        self.humans.append(human)

    def get_count(self):
        return len(self.humans)

    def __eq__(self, other):
        return self.name == other.name

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(f"Creating an instance of {cls.__name__}")
        return instance

human1 = Human("Denys", 1999)
human2 = Human("Denys", 1999)
human3 = Human("Sasha", 1997)
print(human1,",",human1.get_age(),"years")

planet1 = Planet("Mars")

planet1.add_human(human1)
planet1.add_human(human2)
planet1.add_human(human3)

planet2 = Planet("Jupiter")

planet2.add_human(human1)
planet2.add_human(human2)


print(planet1, f"and number of humans on the planet: {planet1.get_count()}")

print(human1==human2, planet1==planet2)
