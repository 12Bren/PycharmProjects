name= "Ford"
print("Hello "+name)

age = 23
age = age + 1
age += 1
# print(type(age))
print("your age is "+str(age))

height = 250.23
print("your height is "+str(height)+"cm")

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

