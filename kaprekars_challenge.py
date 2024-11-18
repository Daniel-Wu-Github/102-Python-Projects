#Use the following letter to number conversions in your program: a > 4, e > 3, o > 0, s > 5, t > 7
#Example output (using input howdy aggies whoop):
#Enter some text: howdy aggies whoop
#In leet speak, "howdy aggies whoop" is:
#h0wdy 4ggi35 wh00p
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
grandSum = 0
def doTheK(x):
    count = 0
    num = str(x)
    numO = num
    sum1 = 0
    while sum1 != 6174:
        sep = []
        inv = []
        for i,k in enumerate(num):
            sep.append(k)
            sep[i] = int(sep[i])
        while len(sep) < 4:
            sep.insert(0, 0)
        sep.sort(reverse=True)
        inverse = sep.copy()
        inverse.sort()
        sep[0]*=1000
        sep[1]*=100
        sep[2]*=10
        inverse[0]*=1000
        inverse[1]*=100
        inverse[2]*=10
        s = sum(sep)
        inv = sum(inverse)
        #print(f"sum is {s}")
        #print(f"inv is {inv}")
        sum1 = s-inv
        num = str(sum1)
        count+=1
        if sum1 == 0:
            break
    return count
for i in range(10000):
    grandSum += doTheK(i)
print(f"Kaprekar's routine takes {grandSum-2} total iterations for all four-digit numbers")
#-2 since 0000 and 9999 shouldn't be counted