import random

# First Problem

f = open("poem.txt")
content = f.read()
if "twinkle" in content:
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")
f.close()




# Second Problem
def game():
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if score > hiscore:
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score
game()


# Third Problem
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


# Fourth Problem
for i in range(2, 21):
    generateTable(i)
    word = "Donkey"
with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("file.txt", "w") as f:
    f.write(contentNew)

# Fivthh Problem
words = ["Donkey", "bad", "ganda", "Anwar"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)


# Six Problem
with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No Python is not present")


# Seven Problem
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No Python is not present")
    

# Eight Problem
with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)

# Nineth Problem
with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else: 
    print("No these files are not identical")



# Nineth Problem
with open("this_copy.txt", "w") as f:
    f.write("")
# Tenth Problem
with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)