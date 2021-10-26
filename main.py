#import time
#---------------indexing[]-----------------#
#name = "craft luis"    [start:stop:step]
#last_name = name[0:10:1] Indexing[]
#-----------------slice()-------------------#
#website = "https://corpby.000webhostapp.com"
#[start:stop:step]
#slice = slice(8,-4) slice()
#print(website[slice])
#--------------if statment------------------#
#age = int(input("how old are you?: "))
#if age == 200:
#    print("your inmortal!!")
#elif age >= 18:
#    print("you are and adult")
#elif age <= 12:
#    print("you have are a child!")
#else:
#    print("you are a teen!")
#-------logical operators (and,or,not)---------------#
#temp = int(input("what is the temperature outside?: "))
#if not(temp >= 0 and temp <= 30):
#   print("the temperature is bad today!")
#    print("stay in side")
#elif not(temp < 0 or temp > 30):
#    print("the temperature is good today")
#    print("lets go outside")
#-------------while loop-------------------------#
#name = ""
#while len(name) == 0:                       while loop = unlimited
#    name = input("type your name?: ")       for loop = limited
#print("hello "+ name)
#name = None
#while not name:
#    name = input("type your name?: ")
#--------------for loop-----------------------------#
#for i in range(10):
#    print(i + 1)
#for i in range(50, 100, 2): #you could use step (start:stop:step)
#    print(i + 1)                                      -END-
#for i in "craft luis":
#    print(i)
#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1)
#print("Happy New Year!!!")
#----------------nested loops------------------------------------------------#
#rows = int(input("how many rows?: "))
#columns = int(input("how many columns?: "))
#sysmbol = input("enter a sysmbol: ")
#for i in range(rows):
#    for j in range(columns):
#        print(sysmbol, end="")
#    print()
#-------------------------how many people would pay--------------------------------------#
#print("Welcome to the tip calculator.")

#bill = input("What was the total bill? $")
#cover = float(bill)

#tip = input("What percentage tip would you like to give? 10, 12, or 15, 4? ")
#cover2 = int(tip)
#cover_tip = cover2 / 100
#remain = float(cover_tip)

#split_bill = input("How many people to split the bill? ")
#cover3 = int(split_bill)

#total = cover * remain
#total2 = cover + total
#total3 = total2
#total4 = total3 / cover3

#total5 = total4
#print(f"Each Person should pay: ${round(total5, 2)}")
#-------------------------------------------------------------------------------------#

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("can ride")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5")
        if age >= 18:
            bill = 12
            print("Please pay $12")
        else:
            bill = 7
            print("Please pay $7")

        want_photo = input("Do you wanna a picture Y or N")
        if want_photo == "Y":
            bill = bill + 3

        print(f"Your total bill will be ${bill}")

else:
    print("can`t ride")
