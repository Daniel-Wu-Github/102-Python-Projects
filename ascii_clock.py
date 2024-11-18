'''Enter the time: 2:56
Choose the clock type (12 or 24): 12
Enter your preferred character: *
*** *** *** A M M
* : * * A A MM MM
*** *** *** AAA M M M
* : * * * A A M M
*** *** *** A A M M
Example output (using inputs 13:49, 24):
Enter the time: 13:49
Choose the clock type (12 or 24): 24
Enter your preferred character:
1 333 4 4 999
11 3 : 4 4 9 9
1 333 444 999
1 3 : 4 9
111 333 4 999'''
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#function to separate tens and ones for the number modeling
def sep(number):
    tens = number // 10
    ones = number % 10
    return tens, ones
#allowed characters
permit = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z', '@', '$', '&', '*','=','']

sp0check = False # made for the special cases 0 o'clock

time = input("Enter the time: ")

Ctype = input("Choose the clock type (12 or 24): ")

char = input("Enter your preferred character: ")
while char not in permit:
    char = input("Character not permitted! Try again: ")

#spliting time into a list of two integers
splitT = time.replace(":"," ")
splitT = splitT.split()
for i in range(2):
    splitT[i] = int(splitT[i])
#modifying the integers if Ctype = 12
isPM = Ctype == "12" and splitT[0] > 12
if isPM:
    splitT[0]-=12
#Check for 0:27 in zybooks
if splitT[0] == 0:
    splitT[0] = 12
    sp0check = True # made for the special cases 0 o'clock
    
#Initializing the entire clock
l1 = "*** ***   *** *** AAA M   M"
l2 = "*** *** : *** *** AAA MM MM"
l3 = "*** ***   *** *** AAA M M M"
l4 = "*** *** : *** *** AAA M   M"
l5 = "*** ***   *** *** AAA M   M"
#############NUMBER MODELS###############
d = {1:[" * ",
        "** ",
        " * ",
        " * ",
        "***"],
     2:["***",
        "  *",
        "***",
        "*  ",
        "***"],
     3:["***",
        "  *",
        "***",
        "  *",
        "***"],
     4:["* *",
        "* *",
        "***",
        "  *",
        "  *"],
     5:["***",
        "*  ",
        "***",
        "  *",
        "***"],
     6:["***",
        "*  ",
        "***",
        "* *",
        "***"],
     7:["***",
        "  *",
        "  *",
        "  *",
        "  *"],
     8:["***",
        "* *",
        "***",
        "* *",
        "***"],
     9:["***",
        "* *",
        "***",
        "  *",
        "***"],
     0:["***",
        "* *",
        "* *",
        "* *",
        "***"]}



#############MODS FOR char###############
#change the characters to the number itself if no character is entered
if char == "":
    for i in d:
        for j,k in enumerate(d.get(i)):
            d.get(i)[j] = k.replace("*",str(i))
else:
    for i in d:
        for j,k in enumerate(d.get(i)):
            d.get(i)[j] = k.replace("*",char)
#############MODS FOR TIME###############
#changing the model before the :
l1 = l1[7:]
l2 = l2[7:]
l3 = l3[7:]
l4 = l4[7:]
l5 = l5[7:]
if splitT[0] < 10:
    l1 = d.get(splitT[0])[0]+l1
    l2 = d.get(splitT[0])[1]+l2
    l3 = d.get(splitT[0])[2]+l3
    l4 = d.get(splitT[0])[3]+l4
    l5 = d.get(splitT[0])[4]+l5
else:
    tens, ones = sep(splitT[0])
    l1 = d.get(tens)[0]+" "+d.get(ones)[0]+l1
    l2 = d.get(tens)[1]+" "+d.get(ones)[1]+l2
    l3 = d.get(tens)[2]+" "+d.get(ones)[2]+l3
    l4 = d.get(tens)[3]+" "+d.get(ones)[3]+l4
    l5 = d.get(tens)[4]+" "+d.get(ones)[4]+l5

#changing the model after the :
if splitT[0] < 10:
    l1 = l1[:5]
    l2 = l2[:5]
    l3 = l3[:5]
    l4 = l4[:5]
    l5 = l5[:5]
else:
    l1 = l1[:9]
    l2 = l2[:9]
    l3 = l3[:9]
    l4 = l4[:9]
    l5 = l5[:9] 
tens, ones = sep(splitT[1])
l1 = l1+" "+d.get(tens)[0]+" "+d.get(ones)[0]
l2 = l2+" "+d.get(tens)[1]+" "+d.get(ones)[1]
l3 = l3+" "+d.get(tens)[2]+" "+d.get(ones)[2]
l4 = l4+" "+d.get(tens)[3]+" "+d.get(ones)[3]
l5 = l5+" "+d.get(tens)[4]+" "+d.get(ones)[4]

#############MODS FOR Ctype (add AM and PM)##############
if (isPM or splitT[0] == 12) and not sp0check: # made for the special cases 0 o'clock
    l1 = l1+" "+"PPP M   M"
    l2 = l2+" "+"P P MM MM"
    l3 = l3+" "+"PPP M M M"
    l4 = l4+" "+"P   M   M"
    l5 = l5+" "+"P   M   M"
if Ctype == "12" and isPM == False:
    l1 = l1+" "+" A  M   M"
    l2 = l2+" "+"A A MM MM"
    l3 = l3+" "+"AAA M M M"
    l4 = l4+" "+"A A M   M"
    l5 = l5+" "+"A A M   M"

print()
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
