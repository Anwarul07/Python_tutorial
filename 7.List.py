friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends)
print(friends[0])
friends[0] = "Grapes"  # Unlike Strings lists are mutable

print(friends[0])
print(friends)
print(friends[1:4])
friends.append("Harry")
print(friends)

l1 = [1, 34, 62, 2, 6, 11]
# l1.sort()
# # l1.reverse()
l1.insert(2, 333333)  # Insert 333333 such that its index in the list is 3
# value = l1.pop(3)
# print(value)
print(l1)
print(type(friends))


# Tupple  are like a string and it is immmutable
a = (1, 45, 342, 3424, False, "Rohan", "Shivam")
b = (2,)
c = 3
print(a)
print(type(a))
print(type(b))
print(type(c))


D = (1, 45, 342, 3424, False, 45, "Rohan", "Shivam")
print(D)

no = D.count(45)

i = D.index(3424)
j = D.index(45)
print("index of 3424 is ", i)
print("count of 45 is ", no)
print("index of 45 is ", j)

print("length of D is ", len(D))


marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()

print(marks)

l = [3, 3, 5, 1]


print(sum(l))
a = (7, 0, 8, 0, 0, 9)

n = a.count(0)
print(n)
