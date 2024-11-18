# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#
n = int(input("Enter a value for n:"))
r = 0
sum1 = 0
left = n - 1
while left != 0:
    sum1 += left
    left -= 1
right = n + 1
sum2 = 0
while sum2 != sum1 and sum2 < sum1:
    sum2 += right
    right += 1
    r+=1
if sum2 == sum1:
    print(f"{n} is a balancing number with r={r}")
else:
    print(f"{n} is not a balancing number")

#Comment