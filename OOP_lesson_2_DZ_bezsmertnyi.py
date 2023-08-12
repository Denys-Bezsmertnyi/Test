#LESSON 2 PRACTICE

# Створити клас Employee.
# __init__ має приймати наступні аргументи: ім’я, ЗП за один робочий день.
# Створити метод work(self, …) який повертає строку “I come to the office.”
# Створити класи Recruiter та Developer, які наслідують клас Employee.
# Перевизначити методи work в класах R та D, щоб вони повертали значення:
# “I come to the office and start to coding.” - для Developer
# “I come to the office and start to hiring.” - для Recruiter
# Перевизначити методи __str__, щоб они повертали строку: “Посада: Ім’я”
# Зробити можливим порівнювати Employee по рівню ЗП.

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

class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."


class Developer(Employee):
    def work(self):
        return "I come to the office and start to coding."


Employee1 = Employee("Denys", 999)
Employee2 = Recruiter("Mark", 550)
Employee3 = Developer("Sofia", 720)
Employee4 = Employee("Sasha", 100)

print(Employee1.work(), '\n', Employee2.work(), '\n', Employee3.work(), sep='')

print(Employee1, '\n', Employee2, '\n', Employee3, sep='')

print(Employee1>Employee4, '\n', Employee2>Employee3, sep='')

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
