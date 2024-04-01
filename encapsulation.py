# Encapsulation is the concept of bunding data and methods with in single unit.
#public class: Accessible anywhere from outside class.
#privet class:
#protect class :


# Data hiding using Encapsulation
class Employee:
    def __init__(self , name , project , salary): 
        self.name = name
        self._project = project
        self.__salary = salary

    def show(self):
        print("Name : ", self.name)

emp =Employee("Madhav", "Xavier", 1000)
emp.show()
print(emp.name)
print(emp._project)
print(emp._Employee.__salary)
      
