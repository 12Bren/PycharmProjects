print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
numberOfPeople = float(input("How many people to split the bill? "))
tipAmount = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
offNum = [12, 10, 15]
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
if tipAmount != offNum[2]:
    billAmount = bill / numberOfPeople
    tipDivided = tipAmount * billAmount / 100
    inTotal = round(billAmount + tipDivided, 2)
    print("Each person should pay: " + "$" + str(inTotal))