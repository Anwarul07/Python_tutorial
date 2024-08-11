# def square(n):
#     return n*n

# Square method using lamda
square = lambda x: x * x
print(square(5))

sum = lambda a, b, c: a + b + c
print(sum(5, 6, 7))

# To join the strings in the lists
a = ["Harry", "Rohan", "Shubham"]

final = "::".join(a)
print(final)
b = ["Harry", "Rohan", "Shubham", "Anwar", "nanhe"]

final2 = "-".join(b)
print(final2)

# formatting
format = "{1} is a good {0}".format("harry", "boy")
print(format)
format = "{0} is a good {1}".format("harry", "boy")
print(format)
