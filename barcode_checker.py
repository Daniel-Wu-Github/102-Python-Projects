# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
fileName = input("Enter the name of the file: ")
barcodes = open(fileName, 'r')
line1 = barcodes.readlines()
line2 = []
for i,j in enumerate(line1):
    line1[i] = j.strip()
for i in line1:
    group1 = []
    group2 = []
    for j,k in enumerate(i[:-1]):
        if j % 2 == 0:
            group1.append(int(k))
        else:
            group2.append(int(k))
    sum1 = sum(group1)
    sum2 = sum(group2)
    num = 10 - int(str(sum2*3 +sum1)[-1])
    if num == int(i[-1]):
        line2.append(i)
count = len(line2)
print("There are",count,"valid barcodes")
barcodes.close()
finalString = "\n".join(line2)
valid_barcodes = open("valid_barcodes.txt","w")
valid_barcodes.write(finalString)
#print(finalString)
valid_barcodes.close()
    
    
    
    
'''Example math using barcode 1877455846014:
Sum of first group = 1 + 7 + 4 + 5 + 4 + 0 = 21
Sum of second group = 8 + 7 + 5 + 8 + 6 + 1 = 35
Multiply second group by 3 = 35 x 3 = 105
Add first group = 105 + 21 = 126
Use the last digit and subtract from ten = 10 - 6 = 4
4 is the last digit in the barcode, so it is valid'''