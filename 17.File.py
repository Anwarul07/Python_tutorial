<<<<<<< Updated upstream
a = open("16.File.txt")
print(a.read())
a.close()


b = open("16.File.txt")
data = b.read()
print(data)
b.close()
=======
# a = open("16.File.txt")
# print(a.read())
# a.close()


# b = open("16.File.txt")
# data = b.read()
# print(data)
# b.close()
>>>>>>> Stashed changes
# File must be closed for good acess


# r is used to show that file is opened is read mode
<<<<<<< Updated upstream
f = open("16.file.txt", "r")
data = f.read()
print(data)
f.close()


# write method for a file
w = open("16.myfile.txt", "w")
new = "hey user this is new file created by io"
w.write(new)
w = open("16.myfile.txt", "r")
print(w.read())
=======
# f = open("16.file.txt", "r")
# data = f.read()
# print(data)
# f.close()


# write method for a file
# w = open("16.myfile.txt", "w")
# new = "hey user this is new file created by io"
# w.write(new)
# w = open("16.myfile.txt", "r")
# print(w.read())
>>>>>>> Stashed changes





<<<<<<< Updated upstream
l=open("16.myfile.txt")
print(l.readline()) #shows the First Line
print(l.readlines())



lines =l.readlines()
print(lines, type(lines)) #shows the liens with data type


f = open("16.myfile.txt")
line = f.readlines()
while(line != ""):
    print(line)
    line =f.readline()  
f.close()
=======
# l=open("16.myfile.txt")
# print(l.readline()) #shows the First Line
# print(l.readlines())



# lines =l.readlines()
# print(lines, type(lines)) #shows the liens with data type


# f = open("16.myfile.txt")
# line = f.readlines()
# while(line != ""):
#     print(line)
#     line =f.readline()  
# f.close()
>>>>>>> Stashed changes



#Append Lines im file
<<<<<<< Updated upstream
add="Hey user this line is added"
append=open("16.File.txt", "a")
append.write(add)
a = open("16.File.txt")
print(a.read())
a.close()
=======
# add="Hey user this line is added"
# append=open("16.File.txt", "a")
# append.write(add)
# a = open("16.File.txt")
# print(a.read())
# a.close()
>>>>>>> Stashed changes


#With  Statements
f = open("16.file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("16.file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file