'''Write a function named parte that takes in as parameters two parallel lists: a list of times (in
increasing order), and a list of distances traveled by that point in time. The function should
return a new list that contains the velocity between consecutive time measurements. The new
list should have a length of one less than the original lists'''
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#function to separate tens and ones for the number modeling
import math
def parta(r_sphere,r_hole):
    h = r_sphere - math.sqrt(r_sphere**2 - r_hole**2)
    vCap = ((1/3)*math.pi*h**2)*(3*r_sphere-h)
    vSphere = (4/3) * math.pi * r_sphere**3 
    holeHeight = (r_sphere*2) - (h*2)
    vHole = holeHeight*math.pi*(r_hole**2)
    vFinal = vSphere - vHole - 2*vCap
    print(vFinal)
    return vFinal
    #comment

def partb(n):
    output = False
    global total
    total = []
    global final
    final = []
    for i in range(1,n,2):
        #if sum(lastI) + i == n:
            #output = True
            #break
        total.append(i)
    for j,k in enumerate(total):
        for l,z in enumerate(total[j:]):
            if sum(total[j:l]) ==  n:
                final = total[j:l].copy()
                output = True
                break
            elif sum(total[j:l+1]) ==  n:
                final = total[j:l+1].copy()
                output = True
                break
    if output:
        return final
    else:
        return output
    #comment
    
def partc(char,name,comp,email):
    global length
    length = max([len(char),len(name),len(comp),len(email)])
    length += 4
    tbBorder = char*(length+2) #+2 for left and right border
    card = f"{tbBorder}"+'\n'+f"{char}{name:^{length}}{char}"+'\n'+f"{char}{comp:^{length}}{char}"+'\n'+f"{char}{email:^{length}}{char}"+'\n'+f"{tbBorder}"
    return card
    #comment

def partd(n):
    minimum = min(n)
    maximum = max(n)
    n.sort()
    if len(n) % 2 == 1:
        median = n[(len(n)//2)]
    else:
        median = (n[(len(n)//2)]+n[((len(n)//2)-1)])/2
    return minimum, median, maximum
    #comment

def parte(a,b):
    global velo
    velo = []
    for j,k in enumerate(b):
        if k != b[-1]:
            velo.append((b[j+1]-b[j])/(a[j+1]-a[j]))
    for l,z in enumerate(velo):
        if z.is_integer():
            velo[l] = int(velo[l])
    return velo
    #comment

def partf(a):
    output = 0
    for j,k in enumerate(a):
        for l,z in enumerate(a[j+1:]):
            if k + z == 2027:
                output = k*z
                break
    return output
    #comment
    
def partg(x,t):
    sum = 0
    n = 1
    y=1
    while abs(y) > t:
        y = (2*(x**(2*n-1)))/(2*n-1)
        n+=1
        sum+=y
    sum-=y
    return sum
print(partg(0.5, 1e-6))
    
            
    