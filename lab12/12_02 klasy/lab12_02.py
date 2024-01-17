# 2. Utworzyć klasę Employee, która dziedziczy po klasie Person
# i zawiera dodatkowy atrybut Age.
# Zdefiniuj metodę displayEmployee(), która wyświetla nazwę pracownika,
# pensję oraz wiek.

from lab12_01 import Person  # lub skopiować daną klasę z pliku lab12_01.py


class Employee(Person):
    def __init__(self, name, salary, age):
        super().__init__(name, salary)
        self.age = age

    def displayEmployee(self):
        print(f"Pracownik {self.name} zarabia {self.salary} w wieku {self.age} lat")


if __name__ == "__main__":
    pracownik1 = Employee("Artur", 5000, 40)
    pracownik1.displayEmployee()
    pracownik1.displayPerson()

    input('press any key -- Employee')
