print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
numberOfPeople = float(input("How many people to split the bill? "))
tipAmount = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
if tipAmount == 10:
    billAmount = bill / numberOfPeople
    tipDivided = 100 / tipAmount
    inTotal = billAmount + tipDivided
    print("Each person should pay: " + "$" + str(inTotal))