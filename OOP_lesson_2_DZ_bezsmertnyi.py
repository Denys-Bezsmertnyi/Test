from datetime import datetime as dt
import csv
import logging
import traceback
import datetime
import requests
import os

from exceptions import EmailAlreadyExistsException

logging.basicConfig(filename=r'C:\Users\gerby\PycharmProjects\pythonProject1\logs.txt', level=logging.ERROR)

class Employee:
    def __init__(self, name, day_salary, email=None):
        self.name = name
        self.day_salary = day_salary
        self.email = email
        if email:
            try:
                self.validate(email)
                self.save_email("emails.csv")
            except EmailAlreadyExistsException:
                print("Email already exists. Logging exception...")
                self.log_exception()


    def save_email(self, emails):
        csv_file_path = os.path.join(os.path.dirname(__file__), 'emails.csv')
        with open(csv_file_path, mode='a', newline='') as file:
            save = csv.writer(file)
            save.writerow([self.email])

    def validate(self, email):
        csv_file_path = os.path.join(os.path.dirname(__file__), 'emails.csv')
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if email in row:
                    raise EmailAlreadyExistsException("Email already exists!")
        print("Email validation successful.")

    def log_exception(self):
        current_datetime = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        traceback_info = traceback.format_exc()
        log_message = f"{current_datetime} | {traceback_info}"
        logging.error(log_message)

    def work(self):
        return "I come to the office"

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}"

    def __gt__(self, other):
        return self.day_salary > other.day_salary

    def __lt__(self, other):
        return self.day_salary < other.day_salary

    def __eq__(self, other):
        return self.day_salary == other.day_salary

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
        base_words = super().work()
        return base_words + "and start to hiring."


class Developer(Employee):
    def __init__(self, name, day_salary, tech_stack):
        super().__init__(name, day_salary)
        self.tech_stack = tech_stack

    def work(self):
        base_words = super().work()
        return base_words + "and start to coding."

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __add__(self, other):
        added_name = self.name + ' ' + other.name
        added_tech_stack = list(set(self.tech_stack + other.tech_stack))
        added_salary = max(self.day_salary, other.day_salary)

        return Developer(added_name, added_salary, added_tech_stack)


employee1 = Employee("Denys", 999, 'gerbyboyz1234@gmail.com')
employee2 = Recruiter("Mark", 550, 'pupochek228124@yahoo.com')
employee3 = Developer("Sofia", 550, ["Python", "JavaScript", "HTML", "CSS"])
employee4 = Developer("John", 800, ["Java", "C#", "C++"])

print(employee1.work(), '\n', employee2.work(), '\n', employee3.work(), sep='')

print(employee1, '\n', employee2, '\n', employee3, sep='')

print(employee1 > employee4, '\n', employee2 > employee3, '\n', employee2 == employee3, sep='')

print(employee1.check_salary())

print(employee3 > employee4)

combined_developer = employee3 + employee4

print(combined_developer.name)
print(combined_developer.tech_stack)
print(combined_developer.day_salary)

class Candidate:
    def __init__(self,first_name,last_name,email,tech_stack,main_skill,main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, file_or_url):
        candidates = []

        if file_or_url.startswith("http://") or file_or_url.startswith("https://"):
            response = requests.get(file_or_url)
            response_text = response.text
        else:
            with open(file_or_url, mode = "r", newline = '') as file:
                response_text = file.read()
        csv_reader = csv.reader(response_text.splitlines())
        next(csv_reader)
        for row in csv_reader:
            full_name, email, tech_stack, main_skill, main_skill_grade = row
            first_name, last_name = full_name.split()
            candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
            candidates.append(candidate)

        return candidates



candidate1 = Candidate('Denys','Bezsmertnyi','denys@gmail.com',['Python','Java'],'Python','Middle')
print(candidate1.full_name)

candidates_csv_path = os.path.join(os.path.dirname(__file__), 'candidates.csv')
candidates_csv = Candidate.generate_candidates(candidates_csv_path)
for candidate in candidates_csv:
    print(candidate.full_name, candidate.email, candidate.tech_stack)

candidates_url = Candidate.generate_candidates('https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')
for candidate in candidates_url:
    print(candidate.full_name, candidate.email, candidate.tech_stack)
