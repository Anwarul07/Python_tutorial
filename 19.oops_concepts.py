class Employee:
    language = "Pyton"  # This is a class attribute
    salary = 1200000

    # self attribute is must for the method
    def getInfo(this):
        print(f"The language is {this.language}. The salary is {this.salary}")

    def greet(self):
        print("Good morning")

    # static method is used to tell compiler to that it not need attributs and run with hight preference with same
    @staticmethod
    def greet():
        print(
            "Good morning via static method which run witouht self props but cant acess the props of class and if name of mtd is same than it prefer more to the @staticmethod"
        )


# Anwar = Employee()
# Anwar.name = "Anwar"  # This is an instance attribute
# print(Anwar.name, Anwar.language, Anwar.salary)

# Raees = Employee()
# Raees.name = "Raees"
# print(Raees.name, Raees.salary, Raees.language)

# # Here name is instance attribute and salary and language are class attributes as they directly belong to the class


# harry = Employee()
# print(harry.language, harry.salary)
# harry.language = "JavaScript"  # This is an instance attribute having more prefrence over class attributes
# print(harry.language, harry.salary)

# Self Attributs
harry = Employee() #=> save as Employee.getInfo(harry)
harry.getInfo()
harry.greet()
harry.greet()

class Employee:
    language = "Pyton"  # This is a class attribute
    salary = 1200000

    # self attribute is must for the method
    def getInfo(this):
        print(f"The language is {this.language}. The salary is {this.salary}")

    def greet(self):
        print("Good morning")

    # static method is used to tell compiler to that it not need attributs and run with hight preference with same
    @staticmethod
    def greet():
        print(
            "Good morning via static method which run witouht self props but cant acess the props of class and if name of mtd is same than it prefer more to the @staticmethod"
        )

    def __init__(self, name, salary, language):  # dunder method which is automatically called each time like a constructor
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")




harry = Employee("Harry", 1300000, "JavaScript") 
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

rohan = Employee("Rhania", 120000, "java")
print(rohan.name, rohan.salary, rohan.language)
