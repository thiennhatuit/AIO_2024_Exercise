from abc import ABC, abstractmethod



class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob
    def get_yob(self):
        return self._yob
    
    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self,name:str,yob:int,grade:str):
        super().__init__(name = name,yob = yob)
        self.__grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name = name, yob = yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self,name:str, yob:int, specialist:str):
        super().__init__(name = name, yob = yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self,name:str):
        self.__name = name
        self.__people_list = list()

    def add_person(self, person:Person):
        self.__people_list.append(person)

    def describe(self):
        print(f"Ward name: {self.__name}")
        for p in self.__people_list:
            p.describe()
    def count_doctor(self):
        counter = 0
        for p in self.__people_list:
            if isinstance(p, Doctor):
                counter += 1
        return counter
    
    def sort_age(self):
        self.__people_list.sort(key = lambda x: x.get_yob(), reverse = True)
    
    def compute_average(self):
        counter = 0
        total_year = 0
        for p in self.__people_list:
            if isinstance(p,Teacher):
                counter += 1
                total_year += p.get_yob()
        return total_year/counter

# Student1 = Student(name ="ThienMinh", yob = 2004, grade = "7")
# Student1.describe()

student1 = Student(name = "Nguyen van a", yob =2004, grade = "7")
student2 = Student(name = "Nguyen Van B", yob = 2005, grade = "10")
student3 = Student(name = "Nguyen Van C", yob = 2004, grade = "12")

teacher1 = Teacher(name = "Truong Van a", yob = 1992, subject="Math")

doctor1 = Doctor(name = "Le Van A", yob = 1995, specialist="Endocrinologists")

ward1 = Ward(name = "Quan Cam")
ward1.add_person(student1)
ward1.add_person(student2)
ward1.add_person(student3)
ward1.add_person(teacher1)
ward1.add_person(doctor1)

ward1.describe()

print("Number of doctor: ", ward1.count_doctor())
print("\nSorted age: ")
ward1.describe()




