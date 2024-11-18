# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
#
# YOUR CODE HERE
#
def calcChange (c):
    penny = 0
    nickel = 0
    dime = 0
    quarter = 0
    while c > 0.009:
        if c >= 0.25:
            c-=0.25
            quarter+=1
        elif c >= 0.10:
            c-=0.10
            dime+=1
        elif c>=0.05:
            c-=0.05
            nickel+=1
        else:
            penny+=1
            c-=0.01
    return(penny, nickel, dime, quarter)

def printChange():
    if quarter > 1:
        print (f"{quarter} quarters")
    elif quarter == 0:
        pass
    else:
        print (f"{quarter} quarter")
    if dime > 1:
        print (f"{dime} dimes")
    elif dime == 0:
        pass
    else:
        print (f"{dime} dime")
    if nickel > 1:
        print (f"{nickel} nickels")
    elif nickel == 0:
        pass
    else:
        print (f"{nickel} nickel")
    if penny > 1:
        print (f"{penny} pennies")
    elif penny == 0:
        pass
    else:
        print (f"{penny} penny")
        
    
pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = pay-cost
change = round(pay-cost,2)
penny, nickel, dime, quarter = calcChange(change)
print(f"You received ${change:.2f} in change. That is...")
printChange()
        
#Comment to self
