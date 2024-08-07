name = "Harry"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)
name = "Harry"

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

name = "harry"

print(len(name)) #counts length of str
print(name.endswith("rry")) #check wheather str is start with or not
print(name.startswith("ha"))#check wheather str is ends with or not
print(name.capitalize()) # Capitiliaze only first letter

a = 'Harry is a good boy\nbut not a bad \'boy\''


print(a)