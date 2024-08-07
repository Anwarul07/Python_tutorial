a = "31.2"
b = float(a)  # a but the type should be float
t = type(b)

print(t)


mine = 10
print(float(mine))
decimal = 405.555
nondecimal = int(decimal)
print(nondecimal)

# Converting the type of data types
integr = 15
print(float(integr))

fisrtnum = input("give the first no ")
secondnum = input("give the second no ")
print("Concatination  of total is  :- ", fisrtnum + secondnum)


# cobnverting of types of input from by default string to int
firstdigit = int(input("write first digit "))
seconddigit = int(input("write second didgit "))
print("sum of all those digiut is :- ", firstdigit + seconddigit)


chek = input("give me a number ")
print(type(chek))

a = int(input("Enter number 1: "))

b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b)
print("Sum is ", a + b)


name = input("pls entered yourt name ")
print(f"Good afternoon {name} ")


# letter = input("pls enter a name ")
# date = input("pls enter date")
# print(
#     f"""
#  Dear {letter},
#  Your are selected . 
#  {date}  """
# )


letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050")) 

name = "Harry is a good  boy and  "

print(name.find("  "))