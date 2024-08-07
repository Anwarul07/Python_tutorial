a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))


if a1 > a2 and a1 > a3 and a1 > a4:
    print("Greatest number is a1:", a1)
elif a2 > a1 and a2 > a3 and a2 > a4:
    print("Greatest number is a2:", a2)
elif a3 > a1 and a3 > a2 and a3 > a4:
 print("Greatest number is a3:", a3)

elif a4 > a1 and a4 > a2 and a4 > a3:
    print("Greatest number is a4:", a4)


# marks check wheather 40% pass or not
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))


# Check for total percentage
total_percentage = (100 * (marks1 + marks2 + marks3)) / 300
if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("You are passed:", total_percentage)
else:
    print("You failed, try again next year:", total_percentage)


# Cheking spam chat
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")
if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This comment is a spam")
else:
    print("This comment is not a spam")



# checking the length of name minimum as 10
username = input("Enter username: ")
if len(username) < 10:
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")



# Cheking spam chat using list
l = ["Harry", "Rohan", "Shubham", "Divya"]
name = input("Enter your name: ")
if name in l:
    print("Your name is in the list")
else:
    print("Your name is not in the list")



# Check for total percentage and indivisual also
marks = int(input("Enter your marks: "))

if marks <= 100 and marks >= 90:
    grade = "Ex"
elif marks < 90 and marks >= 80:
    grade = "A"
elif marks < 80 and marks >= 70:
    grade = "B"
elif marks < 70 and marks >= 60:
    grade = "C"
elif marks < 60 and marks >= 50:
    grade = "D"
elif marks < 50:
    grade = "F"
print("Your grade is:", grade)


# Cheking keyword chat
post = input("Enter the post: ")
if "harry" in post.lower():
    print("This post is talking about harry")

else:
    print("This post is not talking about harry")
