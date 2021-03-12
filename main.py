"""დავალება 1"""

class Calculator:
    @staticmethod
    def add(n1, n2):
        return n1 + n2
    @staticmethod
    def subtract(n1, n2):
        return n1 - n2
    @staticmethod
    def divide(n1, n2):
        return n1 / n2
    @staticmethod
    def multiply(n1, n2):
        return n1 * n2

print(Calculator.add(8, 8), Calculator.subtract(7, 4))

"დავალება 2"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return Calculator.multiply(self.width, self.height)
    def perimeter(self):
        return Calculator.multiply(2, Calculator.add(self.width, self.height))
    def print_info(self):
        print(f'სიგანე {self.width}, სიგრძე {self.height},ფართობი {self.area()}, პერიმეტრი {self.perimeter()}')

"დავალება 3"

class Employee:
    def __init__(self, name, surname, age, salary):
        self.name, self.surname, self.age, self.salary = name, surname, age, salary

    def info(self):
        return f'სახელი {self.name}, გვარი {self.surname}, ასაკი {self.age}, ხელფასი {self.salary}'

employees = []

with open("dataset1.csv", "r") as dataset:
    data = [line.split(",") for line in dataset.readlines()][1:]
    employees = [Employee(name, surname, age, salary) for [name, surname, age, salary] in data]

print(f'ყველაზე დაბალი ხელფასის მქონე თანამშრომელი - {min(employees, key=lambda employee: employee.salary).info()}')
print(f'ყველაზე ასაკოვანი თანამშრომელი - {max(employees, key=lambda employee: employee.age).info()}')