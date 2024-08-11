# # Using walrus operator like a ternery operator
# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)

# # decribes abouit data types
# from typing import List, Union, Tuple 
# n : int = 5           # integer data type
# name: str = "Harry"   #string data type

# def  sum(a: int, b: int) -> int:   #takes arguments as int and return as int
#     return a+b


# #  Match is Like a switch case
# def http_status(status): 
#     match status:  
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500: 
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status"  
# print(http_status(5007))


# # now latest pytjhon can merge multiple dictionary
# dict1 = {'a': 1, 'b': 2} 
# dict2 = {'b': 3, 'c': 4} 
# merged = dict1 | dict2 
# print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}


# # can use multiple file directory in one with method

# # with(
# #     open('file1.txt') as f1,
# #     open('file2.txt') as f2
# # ):
 

#  #try and except to get rid crash of programme and move further with erro hint
# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

# except ValueError as v:
#     print("Heyyyy")
#     print(v)
    
# except Exception as e:
#     print(e) 

# print("Thank You")

# #raising error
# a = int(input("Enter a number: "))
# b = int(input("Enter second number: "))

# if(b == 0):
#     raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
# else:
#     print(f"The division a/b is {a/b}")

# # try and else used when code is good it execute else section
# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

    
# except Exception as e:
#     print(e) 


# else:
#     print("I am inside else")   # This is executed only if the try was successful


# def main():
#  # Try and Final is used when final has to execute at any coast fil try or except, ostly used when it is inside function and try and except return
#  try:
#      a = int(input("Hey, Enter a number: "))
#      print(a)
#      return
        
#  except Exception as e:
#      print(e) 
#      return

#  finally:
#      print("Hey I am inside of finally")

# main()


# scope of a variable
a = 89

def fun(): 
    global a # makes global inside func an dmake it loacal value
    a = 3
    print(a)
    
# print(a)
fun()
print(a)

#  enumerate function
l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")


# List _comprehensions
myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)