# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
def checker(s):
    if s[:3] == "byr":
        if int(s[4:]) >= 1920 and int(s[4:]) <= 2007:
            return True
        else:
            return False
    if s[:3] == "iyr":
        if int(s[4:]) >= 2013 and int(s[4:]) <= 2023:
            return True
        else:
            return False
    if s[:3] == "eyr":
        if int(s[4:]) >= 2023 and int(s[4:]) <= 2033:
            return True
        else:
            return False
    if s[:3] == "hgt":
        if s[-2:] == "in":
            t = s[:-2]
            if int(t[4:]) >= 59 and int(t[4:]) <= 76:
                return True
            else:
                return False
        elif s[-2:] == "cm":
            t = s[:-2]
            if int(t[4:]) >= 150 and int(t[4:]) <= 193:
                return True
            else:
                return False
        else:
            return False
    if s[:3] == "hcl":
        if s[4] == '#' and all(c in "0123456789abcdef" for c in s[5:]) and len(s[5:]) == 6:
            return True
        else:
            return False
    if s[:3] == "pid":
        if len(s[4:]) == 9:
            return True
        else:
            return False
    if s[:3] == "cid":
        t = s[4:]
        if t[0] == "0":
            t1 = t[1:]
        else:
            t1 = t
        if len(t1) == 3:
            return True
        else:
            return False
newList = []
inventory = []
inventory_check = []
inventory_check2 = []
required = ["byr","iyr","eyr","hgt",'hcl',"pid","cid"]
fileName = input("Enter the name of the file: ")
passports = open(fileName, 'r')
line1 = passports.readlines()
combined = "".join(line1)
list1 = combined.split("\n\n")
count0 = len(list1)
for j in list1:
    if all(i in j for i in required):
        newList.append(j)
count = len(newList)
finalString = "\n\n".join(newList)
passports.close()
#print("There are",count,"valid passports")
valid_passports = open("valid_passports.txt","w")
valid_passports.write(finalString)
#print(finalString)
valid_passports.close()
#############################PartB
for i in newList:
    j = i.replace("\n"," ")
    inventory.append(j.split(" "))
for i,l in enumerate(inventory):
    for j,k in enumerate(l):
        if checker(k) == False:
            break
    else:
        inventory_check.append(l)
        inventory_check2.append(newList[i])
count2 = len(inventory_check)
print("There are",count2,"valid passports")
finalString2 = "\n\n".join(inventory_check2)
valid_passports2 = open("valid_passports2.txt","w")
valid_passports2.write(finalString2)
valid_passports2.close()
'''byr – Birth year – four digits, between 1920 and 2007, inclusive
• iyr – Issue year – four digits, between 2013 and 2023, inclusive
• eyr – Expiration year – four digits, between 2023 and 2033, inclusive
• hgt – Height – a number followed by either cm or in
o If cm, the number must be between 150 and 193, inclusive
o If in, the number must be between 59 and 76, inclusive
• hcl – Hair color – a # followed by exactly 6 characters (0-9 or a-f)
• ecl – Eye color – not required
• pid – Passport ID – a nine-digit number, including leading zeroes
• cid – Country ID – a three-digit number, NOT including leading zeroes'''