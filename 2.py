import numpy as np
matrix = open("module12quizF23.txt","r")
matrices = matrix.readlines()
matrix.close()
for i,j in enumerate(matrices):
    matrices[i] = int(j.strip())
array = np.array(matrices).reshape(100,100)
key = [
array[0:5,85].sum()
,int(array[4].sum()/100)
,array[62,-5:].sum()
,array[0].min()
,array[29].max()
]

keyletters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
finalkey=""
def getindex(char):
    for i,j in enumerate(keyletters):
        if j == char:
            return i
def getletter(num):
    if num > 25:
        num-=25
    return keyletters[num]
for i in key:
    finalkey+=keyletters[i]
print("key is",finalkey)
message = "zilhpzsyucavkzbf"
finalkey*=100
finalkey = finalkey[:len(message)]
answer = []
messageIndex = []
for i,j in enumerate(message):
    messageIndex.append(getindex(j))
for i,j in enumerate(finalkey):
    answer.append(getletter(messageIndex[i]-getindex(j)))
output = "".join(answer)
print("output is",output)