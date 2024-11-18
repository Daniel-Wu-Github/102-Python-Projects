# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR

from time import time
import math
total = []
SQ1 = []
def getSQ(num):
    SQ = []
    for x in range(0,num+1):
        if math.sqrt(x).is_integer():
            SQ.append(x)
    return SQ
def list_nums(num):
    total = []
    for x in range(0,num+1):
        if math.sqrt(x).is_integer():
            SQ1.append(x)
    for a,q in enumerate(SQ1(num)):
        for b,w in enumerate(SQ1(num)[a:]):
            for c,e in enumerate(SQ1(num)[b:]):
                for d,r in enumerate(SQ1(num)[c:]):
                    if q + w + e + r == num:
                        total.append(int(math.sqrt(q)))
                        total.append(int(math.sqrt(w)))
                        total.append(int(math.sqrt(e)))
                        total.append(int(math.sqrt(r)))
                        return total
                    
def count_sets(num):
    sets=0
    bank = []
    for a,q in enumerate(getSQ(num)):
        for b,w in enumerate(getSQ(num)[a:]):
            for c,e in enumerate(getSQ(num)[b:]):
                for d,r in enumerate(getSQ(num)[c:]):
                    if q + w + e + r == num:
                        total = []
                        total.append(int(math.sqrt(q)))
                        total.append(int(math.sqrt(w)))
                        total.append(int(math.sqrt(e)))
                        total.append(int(math.sqrt(r)))
                        if sorted(total) not in bank:
                            sets+=1
                            bank.append(total)
                            print("total is now",total)
                            continue
    return sets

    
# how to measure how long your function takes to run:
t1 = time() # get start time
print(count_sets(27))# run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result