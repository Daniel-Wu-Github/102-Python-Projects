# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
light = " "
fileName = input("Enter the filename: ")
dark = input("Enter a character: ")
pixels = open(fileName, 'r')
art = pixels.readlines()
pixels.close()
pixel_art = open(f"{fileName[:-4]}.txt","w")
for i,j in enumerate(art):
    art[i] = j.strip().split(",")
for i,j in enumerate(art):
    for k,l in enumerate(j):
        j[k] = int(l)
for i,j in enumerate(art):
    for k,l in enumerate(j):
        if k % 2 == 0:
            for p in range(0,l):
                #print(light,end="")
                pixel_art.write(light)
        else:
            for p in range(0,l):
                #print(dark,end="")
                pixel_art.write(dark)
    #print()
    if i != (len(art)-1):
        pixel_art.write("\n")
pixel_art.close()
print(f"{fileName[:-4]}.txt created!")
'''pixel_art = open(f"{fileName[:-4]}.txt","r")
art2 =pixel_art.readlines()
print(art2)'''

        
    











'''Write a program named pixel_painter.py that takes as input a filename and a character, converts the contents
of the file to pixel art using a space for light pixels and the entered character for dark pixels, and writes the art
to a new file of the same name but with the .txt extension.
Example pixel_triangle.csv file:
2,1,2
1,1,1,1,1
0,5
Example output using inputs pixel_triangle.csv and A:
Enter the filename: pixel_triangle.csv
Enter a character: A
pixel_triangle.txt created!
Example pixel_triangle.txt file created by your program:
A
A A
AAAAA'''