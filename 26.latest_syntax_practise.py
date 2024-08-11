# # By default it takes auto correct indexs otherwise have toi mention
# name = input("Enter name: ")
# marks = int(input("Enter marks: "))
# phone = int(input("Phone number: "))

# s = "The name of the student is {}, his marks are {} and phone number is {}".format(
#     name, marks, phone
# )
# print(s)

# # Multiplicatio of number
# table = [str(7 * i) for i in range(1, 11)]

# s = "\n".join(table)
# print(s)


# # Filter to find number divisible by number
# def divisible5(n):
#     if n % 5 == 0:
#         return True
#     return False


# a = [1, 2, 34234, 53, 6234235, 64343, 65, 754, 45, 55]

# f = list(filter(divisible5, a))
# print(f)
# print(f)

# # filetr to gretest number
# from functools import reduce

# l = [111, 2, 65, 5553, 635, 65, 74, 45, 55]


# def greater(a, b):
#     if a > b:
#         return a
#     return b


# print(reduce(greater, l))


#flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World! anwar, This is first flask app </p>"

app.run()

