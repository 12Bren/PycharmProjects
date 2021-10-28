import math
# day one
print("Hello world \n" * 3)
print("Hello " + "Bren")
# print("what is your name? " + input())
# Write your code below this line 👇 Assignment 11
# name = input("what is your name? ")
# print("Hello " + name), print("there are " + str(len(name)) + " characters in your name!")
# The computer reads this like:  name = input("what is your name? ") prints "what is your name? " to user
# User defines name (bren) so name = bren computer replaces name with "bren".
# moves to next line print("Hello " + name) since "name" is defined computer prints "hello bren"
# computer moves to next line then sees the next print statement. first "there are " +
# stopping here wasn't completely right. Will try again
# switching variables outcome: assignment 13.1
# 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
# a1 = b
# b1 = a
# a = b1
# b = a1
#Write your code above this line 👆
####################################
# 🚨 Don't change the code below 👇
print("a: " + "a")
print("b: " + "b")
# answer to the teachers hint (If you had a cup of coffie and a glass of milk how would you switch them?)
# answer: place the contents of one cup into a new cup and do the same for the remaining cup. This will give you 4
# cups in total. Then switch and place the contents of the opposite cup into the two first cups
# answer was almost correct 1 too many cups
# How the computer read the code a = input("a: ") grabs a: and runs input after user input (3) variable a is now 3
# same is done for b = input("b: ") b (5) b is 5. next line a1 = b then a1 = 5 b1 = 3
# next line- a = b1 b1 is 3 so a now equals 3, next line- b = a1 a1 = 5 so b = 5
# next line- print("a: " + a) computer sees print command reads whats in parenthesis and reads from left to right
# a: + a reduced to a: 3 then reads the print command and prints a: 3
# next line- print("b: " + b) computer sees print command, encapsulates the whole command, moves inside the parenthesis,
# reads from left to right, b:, executes concatenation (str b: + 5 = b: 5), moves to print command, executes print,
# end result b: 5
# day 1 final project
# print("Welcome to the Band Name Generator.")  # read: Welcome to the Band Name Generator., then prints
# cityName = input("What's the name of the city you grew up in? \n")  # read: What's the name of the city you grew up in?,
# brakes line, executes input, cityName = input
# petName = input("What's your pet's name? \n")  # read: What's your pet's name?, breaks line, executes input,
# petName = input
# print("Your band name could be " + cityName + " " + petName)  # read: Your band name could be, concatenates cityName,
# concatenates " ", concatenates petName, Your band name could be cityName petName, executes print, compilation finished
# END OF DAY 1:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# DAY 2: data types
# test code final
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
numberOfPeople = float(input("How many people to split the bill? "))
tipAmount = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
offNum = 12, 10, 15
if tipAmount == 10:
    billAmount = bill / numberOfPeople
    tipDivided = tipAmount*billAmount / 100
    inTotal = round(billAmount + tipDivided, 2)
    print("Each person should pay: " + "$" + str(inTotal))
if tipAmount == 12:
    billAmount = bill / numberOfPeople
    tipDivided = tipAmount * billAmount / 100
    inTotal = round(billAmount + tipDivided, 2)
    print("Each person should pay: " + "$" + str(inTotal))
if tipAmount == 15:
    billAmount = bill / numberOfPeople
    tipDivided = tipAmount * billAmount / 100
    inTotal = round(billAmount + tipDivided, 2)
    print("Each person should pay: " + "$" + str(inTotal))
if tipAmount != offNum:
    billAmount = bill / numberOfPeople
    tipDivided = tipAmount * billAmount / 100
    inTotal = round(billAmount + tipDivided, 2)
    print("Each person should pay: " + "$" + str(inTotal))




