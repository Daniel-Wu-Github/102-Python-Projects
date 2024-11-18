# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Gabriel Deem
# Daniel Wu
# Erica Yi
# Madelynn Johnson
# Section: 564
# Assignment: Lab 3.15
# Date: 31/8/2023
def N (q):
    q*= 4.4482216152605
    return(q)
def F (q):
  q*=3.280839895
  return (q)

def kPa (q):
  q*=101.325
  return (q)

def BTU (q):
  q*=3.41214163
  return (q)

def G (q):
  q = q*0.264172052*60
  return (q)

def Far (q):
  q = q*(9/5)+ 32
  return (q)

quan = float(input("Please enter the quantity to be converted:"))
print()
print(f"{quan:.2f} pounds force is equivalent to {N(quan):.2f} Newtons")
print(f"{quan:.2f} meters is equivalent to {F(quan):.2f} feet")
print(f"{quan:.2f} atmospheres is equivalent to {kPa(quan):.2f} kilopascals")
print(f"{quan:.2f} watts is equivalent to {BTU(quan):.2f} BTU per hour")
print(f"{quan:.2f} liters per second is equivalent to {G(quan):.2f} US gallons per minute")
print(f"{quan:.2f} degrees Celsius is equivalent to {Far(quan):.2f} degrees Fahrenheit")
#comment
