import math

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

# name = input("Type your name: ")  # all data input is of the str data type by default
# print("Hello " + name)

# age = input("How old are you?: ")  # will always throw an error because input can only be a str
# age = int(input("What is your age?: "))  # by specifying what data type the input will be we can go around
age += 1
# height = float(input("How tall are you? "))

# print("you are " + str(age) + " years old")  # str's can never be output with int therefore age is changed
# print("and your height is " + str(height) + "cm welcome to the tall club!:P")
print(age)
# --------------------------------------------------------
# functions within the math module
pi = 3.14
d = 5
k = 1
u = 25
sum = d, k, u
print(round(pi))
print(math.ceil(pi))  # round up
print(math.floor(pi))  # round down
print(abs(pi))  # gives absolute value tells how far away a nu,ber is from 0
print(pow(pi, 3))  # pi to the power of 3
print(math.sqrt(420))  # square root function
print(max(sum))  # find largest value between d k u
print(min(sum))  # finds minimum value
# ----------------------------------------------------------
# str slicing or creating a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

tame = "nope ho"
first_name = tame[0:4]  # [:4] would work too
last_name = tame[4:7]
test = tame[:5:2]  # [::2]would work too as beginning and end of string
reversed_name = tame[::-1]  # reversed string is read [start: stop: step] or [beginning:end:move up/down]

print(reversed_name)
# practical use for slicing using the slice() function to create a reusable slice object:
website = "http://duckduckgo.com"
website2 = "http://yourgametwo.com"
slice = slice(7, -4)  # initializing slice object slice(beginning,end)

print(website[slice]+" "+website2[slice])
# if statements


