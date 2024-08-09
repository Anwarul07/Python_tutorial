# Printing a def to find greatest number
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

# a = 1
# b = 23
# c = 3

# print(greatest(a, b, c))
print(greatest(10, 12, 11))

#Forenhight to celcuios convertor
def f_to_c(f):
    return 5*(f-32)/9

f= int(input("Enter tempreature "))
print(f_to_c(f))


#Forenhight to celcuios convertor
def g(t):
  print(f"The tempreature is {5*(t-32)/9}°C")
g(100)


#Forenhight to celcuios convertor
def g(t):
  print(f"The tempreature is {5*(t-32)/9}°C")

f= int(input("Enter tempreature "))
g(f)

#Removing extra line 
print("a")
print("b")
print("c", end="")
print("d", end="")

# N natural numbers sum
def sum_natural(n):
    if n == 1:
        return 1
    return sum_natural(n - 1) + n
print(sum_natural(5))

#Star pattern print using Recursion
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(7)


#inch to cm convertor
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")


#inch to cm convertor
def inch_to_cm(inchi):
    return inchi*2.54
print(inch_to_cm(10))
