# Multiplication of a number
# i = 1
# n = 5
# while i < 11:
#     print(f"The Prdouct of {n}x{i} = ", n * i)
#     i += 1

#Multiple table of a number
n=7
for j in range(1,11):
   print(f"The Prdouct of {n}x{j} = {n* j}")



#Multipe table of a number in reverse Order
n=7
for j in range(1,11):
   print(f"The Prdouct of {n}x{11-j} = {n* (11-j)}")

name = [
    "Anwar",
    "Haidar",
    "Sohail",
    "Arbaz",
    "Gulam",
]
for name in name:
    if name.startswith("A"):
        print(f"Hello {name}")

# prime number
number= int(input("Enter the number "))
for j in range(2,number):
    if(number%j)==0:
        print("NO, This is not a prime no")
        break;
else:
  print("This is a prime number ")


n = int(input("Enter number "))
i=1
sum= 0
while (i <= n):
    sum+=i
    i += 1
print(sum)

#Factorila find
n = int(input("Enter number "))
product=1
for i in range(1, n+1):
    product= product*i
print(f"factorial opf the numbr is {product}")


# #making star Pattern
n = int(input("Enter number "))
for i in range(1, n+1):
       
    print(""*(n-1), end="")
    print("*"*(2*i-1), end="")
    print("")



#making star Pattern
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    print("*"* i, end="")
    print("")



'''

***
* *       for n = 3
***


'''
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")