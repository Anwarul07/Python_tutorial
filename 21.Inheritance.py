class Employee:
    company = "ITC"

    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(
            f"The name of the Employee base is {self.name} and the salary is {self.salary}"
        )


class Programmer(Employee):
    company = "ITC Infotech"

    def showderived(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of  showderived derived is {self.name} and the salary is {self.salary}")

    def showLanguage(self,name,language):
         self.name = name
         self.language = language
         print(f"The name of showlanguage derived is {self.name} and he is good with {self.language} language")


b = Programmer()
a = Employee()
a.show("unknown base a", 25000)
print(a.company)
b.show("unknown derived inherit base", 55000)
print(b.company)
b.showderived("unknown showderived derived", 100)
b.showLanguage("unknown showlang derived", "java")



# Multi level inheritance
class Employee:
    a = 1 

class Programmer(Employee):
    b = 2 

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)

# super keyword in inheritance to called the parents class contructor
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)

# class method  attributes to prefer class object instead of object object(instance value) @classmethod uses cls instead of self
class Employee:
    a = 1 #due to @classmethod this value will not show after initialize object value
    
    @classmethod  #due to @classmethod this value will not show after initialize object value
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45 #due to @classmethod this value will not show 

e.show()




# Getter and Setter
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname, e.lname)

e.show()

# Property decorator
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)