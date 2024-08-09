def sum():
    a= int(input("pls enter first number "))
    b= int(input("pls enter the second number "))
    c =int(input("pls enter the third number "))
    average= (a+b+c)/3
    print(average)


sum()


def Multiple(a,b,c):
    Result=a*b*c
    print(Result)

Multiple(2,3,4)

def greet():
    print("Greet from my self ")
greet()


def better(name, marks):
    print(F"Hello welcome {name} to my def function")
    print(F"Your marks is {marks} ")
    print("Thank You")
    return "ok worked"

f=better("Anwar", "70%")
print(f)


def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"

d=goodDay("Harry", "Thank you")
print(d)


def store():
    return "ok"
store()

def defination():
    print("retuning a sentances")
defination()

#Default arguments


factorial(n) = n * factorial(n-1)


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

f= factorial(5)
print(f)

n = int(input("Enter a number:  "))
print(f"The factorial of this number is: {factorial(n)}")