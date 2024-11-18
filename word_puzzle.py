# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Wu
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")
def get_valid_letters(a):
    global bank
    bank = []
    for i in a:
        if i not in bank and i.isalpha():
            bank.append(i)
    bank = "".join(bank)
    return bank
def is_valid_guess(bank,a):
    global close
    close = True
    output = True
    if len(a) == len(bank):
        for i in a:
            if i not in bank:
                output = False
                close = False
        for i in bank:
            if i not in a:
                output = False
    else:
        output = False
        close = False
    return output  
def check_user_guess(d,q,v,r):
    if d == (q*v)+r:
        return True
    else:
        return False
def make_number(word,key):
    answer = []
    for i in word:
        for j,k in enumerate(key):
            if k == i:
                answer.append(j)
    for l,z in enumerate(answer):
        answer[l] = str(z)
    answer = "".join(answer)
    answer = int(answer)
    return answer
def make_numbers(puzzle,guess):
    puzzle = puzzle.split(" | ")
    qv = puzzle[0].split(",")
    q = qv[0]
    v = qv[1]
    d = puzzle[1].split(",")[0]
    r = puzzle[1].split(",")[-1]
    d1 = make_number(d,guess)
    q1 = make_number(q,guess)
    v1 = make_number(v,guess)
    r1 = make_number(r,guess)
    return d1,q1,v1,r1
def main():
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)  
    bank1 = get_valid_letters(puzzle)
    guess = input("\nEnter your guess, for example ABCDEFGHIJ: ")
    if is_valid_guess(bank1, guess) == False:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        if check_user_guess(*make_numbers(puzzle, guess)) == False:
            print ("Try again!")
        else:
            print("Good job!")

if __name__ == '__main__':
        main()
#comment