# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
newList = []
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
print("There are",count,"valid passports")
valid_passports = open("valid_passports.txt","w")
valid_passports.write(finalString)
#print(finalString)
valid_passports.close()