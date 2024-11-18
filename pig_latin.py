# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Daniel Wu
# Section: 564
# Assignment: Lab 2.11
# Date: 24th August 2023
#If a word starts with a consonant (or cluster of consonants that form one sound), move the
#consonant(s) to the end of the word, and add “ay” to the end
# Example: “computer” becomes “omputercay”
# If a word starts with a vowel, add “yay” on to the end of the word
# Example: “engineering” becomes “engineeringyay”
#Note: treat “y” as a vowel for this assignment
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y']
eng = input("Enter word(s) to convert to Pig Latin:")
engList = eng.split()
print(f'In Pig Latin, "{eng}" is: ', end="")
for w in engList:
    letter0 = w[:1]
    if letter0 in vowels:
        w+="yay"
        print(w, end=" ")
    else:
        i = 0
        while w[i] not in vowels:
            i += 1
        rest = w[i:]
        rest += w[:i]
        rest += "ay"
        print(rest, end=" ")
#comment