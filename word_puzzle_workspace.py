
"""
Create a function named main that does not take in any arguments nor return any values. This
function should take as input from the user a puzzle string, print the puzzle, ask the user to
enter a guess, and output an appropriate message. Your main function should call your
get_valid_letters, is_valid_guess, make_numbers, and check_user_guess functions, as well as
the provided print_puzzle function. Format your output as shown below.
"""
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
    print_puzzle(puzzle)    
    bank1 = get_valid_letters(puzzle)
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    while is_valid_guess(bank1, guess) == False:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
        guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    while check_user_guess(*make_numbers(puzzle, guess)) == False:
        print ("Try Again!")
        guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    print("Good job!")
print("1 is",get_valid_letters("RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"))
print("2 is",is_valid_guess("RUEAMOSIKT","IMAKEIMAKE"))
print("3 is",check_user_guess(10,2,3,4))
print("4 is",make_number("RUE","TAKEOURSIM"))
print("5 is",make_numbers("RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA","TAKEOURSIM"))
main()