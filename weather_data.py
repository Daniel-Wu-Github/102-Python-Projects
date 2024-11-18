# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
def getMonth(s):
    if s == "January":
        return "1"
    elif s == "February":
        return "2"
    elif s == "March":
        return "3"
    elif s == "April":
        return "4"
    elif s == "May":
        return "5"
    elif s == "June":
        return "6"
    elif s == "July":
        return "7"
    elif s == "August":
        return "8"
    elif s == "September":
        return "9"
    elif s == "October":
        return "10"
    elif s == "November":
        return "11"
    elif s == "December":
        return "12"
Max = 0
Min = 0
pool = []
denominator = 0
enumerator = 0
pcount = 0
data = open("WeatherDataCLL.csv", 'r')
alldata = data.readlines()
trim = alldata[1:]
for i,j in enumerate(trim):
    trim[i] = j.split(",")
for i in trim:
    if i[5] != "" and int(i[5]) > Max:
        Max = int(i[5])
Min = Max
for i in trim:
    t = i[6].strip()
    if t != "" and int(t) < Min:
        Min = int(t)
print(f"10-year maximum temperature: {Max} F")
print(f"10-year minimum temperature: {Min} F")
print()
month = input("Please enter a month: ")
year = input("Please enter a year: ")
print()
print(f"For {month} {year}:")
month = getMonth(month)
for i,j in enumerate(trim):
    for k,l in enumerate(j):
        temp = l.split("/")
        if temp[0] == month and temp[2] == year:
            pool.append(j)
        break
for i,j in enumerate(pool):
    if j[4] != "":
        enumerator += int(j[4])
        denominator += 1
mADT = enumerator/denominator
denominator = 0
enumerator = 0
for i,j in enumerate(pool):
    if j[3] != "":
        enumerator += float(j[3])
        denominator += 1
mARH = enumerator/denominator
denominator = 0
enumerator = 0
for i,j in enumerate(pool):
    if j[1] != "":
        enumerator += float(j[1])
        denominator += 1
mDWS = enumerator/denominator
denominator = 0
enumerator = 0 
for i,j in enumerate(pool):
    if float(j[2])!=0:
        pcount +=1
pP = (pcount/len(pool))*100
print(f"Mean average daily temperature: {mADT:.1f} F")
print(f"Mean relative humidity: {mARH:.1f} %")
print(f"Mean daily wind speed: {mDWS:.2f} mph")
print(f"Percentage of days with precipitation: {pP:.1f} %")
#comment