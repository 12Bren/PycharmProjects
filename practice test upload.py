name = "Ford"
print("Hello " + name)

age = 23
age = age + 1
age += 1
# print(type(age))
print("your age is " + str(age))

height = 250.23
print("your height is " + str(height) + "cm")

human = False
print("Are you a human? " + str(human))
print(type(human))
# -------------------------------------------
# Multiple assignment practice. assigns multiple variables on the same line

name = "sop"
age = 22
attractive = True
# now the above information referenced in multiple assignment
name, age, attractive = "sop", 22, True

spongbob = 30
patrick = 30
sandy = 30
dog = 30
spongbob = patrick = sandy = dog = 30
# ----------------------------------------------
# string methods
name = "nope spoe"
print(len(name))
print(name.find("spoe"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())  # checks is string contains alphabetical letter will not work if spaces are present
print(name.count("o"))  # counts how many times a character is present within str
print(name.replace("o", "a"))  # specifies first which letter to change second what the letter is replaced with
print(name * 5)
# ---------------------------------------------------
# Type casting in python. Converting 1 data type to another

x, h, i = 4, "Hello", 2.6  # letters cannot be type cast
i = int(i)
x = float(x)
i = str(i)
print(x, h, type(i))
# ----------------------------------------------------
# input

name = input("Type your name: ")  # all data input is of the str data type by default
print("Hello " + name)

# age = input("How old are you?: ")  # will always throw an error because input can only be a str
age = int(input("What is your age?: "))  # by specifying what data type the input will be we can go around
age += 1
height = float(input("How tall are you? "))

print("you are " + str(age) + " years old")  # str's can never be output with int therefore age is changed
print("and your height is " + str(height) + "cm welcome to the tall club!:P")
print(age)
# --------------------------------------------------------
