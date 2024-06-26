class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    def compute_salary(self):
        return self._salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        self._name = name
        self._salary = salary
        self.__bonus = bonus

    def compute_salary(self):
        return super().compute_salary() + self.__bonus
    
mai = Manager('Mai', 100,50)
salary = mai.compute_salary()
print(salary)