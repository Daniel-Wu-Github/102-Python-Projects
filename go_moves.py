board = [["."]*19 for _ in range(19)]
string = ''
for x in range(19):
    for y in range(19):
        string += board[x][y]
    string += '\n'
print(string)
count = 2
x = input("Enter the column number for your stone: ")
y = input("Enter the row number for your stone: ")

while (x != "stop" and y != "stop"):
    x = int(x)
    y = int(y)
    if (x < 0 or x > 8 or y < 0 or y > 8):
        print("Can't place on board because it's out of range, try again!")
    elif board[x][y] == ".":
        if (count % 2 == 0):
            board[x][y] = "●"
        else:
            board[x][y] = "○"
        count += 1
    else:
        print("This space is occupied, please try again")
    string = ''
    for x in range(9):
        for y in range(9):
            string += board[x][y]
        string += '\n'
    print(string)
    x = input("Enter the column number for your stone: ")
    y = input("Enter the row number for your stone: ")
