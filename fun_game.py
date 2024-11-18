import turtle
import time
import numpy as np
turtle.TurtleScreen._RUNNING=True

global moveMemory
moveMemory = []
global blackCapCount
global whiteCapCount
global isActive
blackCapCount = 0
whiteCapCount = 0
isActive = False

def draw_board():
    turtle.TurtleScreen._RUNNING=True
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.bgcolor("white")

    # Draw horizontal lines and label them
    for i in range(-270, 300, 30):
        turtle.penup()
        turtle.goto(-270, i)
        turtle.pendown()
        turtle.forward(540)
        turtle.penup()
        turtle.goto(-300, i - 15)  # Adjusted y-coordinate to position the numbers correctly
        turtle.write(str(20 - (i + 300) // 30), align="right")

    # Reset position and orientation
    turtle.penup()
    turtle.goto(-270, 270)
    turtle.right(90)

    # Draw vertical lines and label them
    for i in range(-270, 300, 30):
        turtle.penup()
        turtle.goto(i, 270)
        turtle.pendown()
        turtle.forward(540)
        turtle.penup()
        turtle.goto(i + 5, 285)
        turtle.write(str((i + 300) // 30), align="center")
    turtle.TurtleScreen._RUNNING = True

def place_piece(row, col, color):
    turtle.TurtleScreen._RUNNING=True
    turtle.speed("fastest")
    x = -270 + col * 30
    y = 270 - row * 30

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(30, color)
    turtle.TurtleScreen._RUNNING = True
def menu():
    '''Print the available options as the menu with a border'''
    border = "#" + "*"*34 + "#"
    
    print(border)
    print("|  Option 1: Read Instructions     |")
    print("|  Option 2: Start New Game        |")
    print("|  Option 3: See Captured Pieces   |")
    print("|  Option 4: Proceed with Your Turn|")
    print("|  Option 5: Quit Game             |")
    print(border)
    print()


def readInstructions():
    '''Read the Rules file and prints it'''
    print()
    print("You have chosen option 1")
    print()
    print()
    time.sleep(2)
    rules = open("Rules of the Game.txt","r")
    print(rules.read())
    rules.close()
    print()
    print("------------------------------------------------------------------")
    print()
    time.sleep(2)
    print("Now Choose Your Next Option")
    print()

def newGame():
    '''Start a New Game'''
    global isActive
    isActive = True
    turtle.TurtleScreen._RUNNING=True
    print()
    print("You have chosen option 2")
    print()
    global moveMemory
    moveMemory = []
    print("Welcome to Pente")
    draw_board()
    turtle.done()
    print("------------------------------------------------------------------")
    print("Please enter your desired placement by indicating the row number, the column number, and the color of your piece. Each input should be separated by one single space.")
    print()
    print("Example Format: (please enter all lowercase for the color)")
    print("Row# Clomun# color")
    print("------------------------------------------------------------------")
    print()
    nextMove()
    time.sleep(2)
    turtle.TurtleScreen._RUNNING=True

def captured():
    global blackCapCount
    global whiteCapCount
    print()
    print("You have chosen option 3")
    print()
    print(f"{blackCapCount} black pieces have been captured")
    print(f"{whiteCapCount} white pieces have been captured")
    print()

def nextMove():
    global moveMemory
    turtle.TurtleScreen._RUNNING=True
    print()
    print("You have chosen option 4")
    print()
    entry = input("Please Enter the Coordinates and the Color: ")
    entry = entry.split(" ")
    entry[0] = int(entry[0])-1
    entry[1] = int(entry[1])-1
    if entry not in moveMemory:
        moveMemory.append(entry)
        draw_board()
        for line in moveMemory:
            place_piece(int(line[0]), int(line[1]), line[2])
        turtle.done()
        turtle.TurtleScreen._RUNNING=True
        print()
        print("Your Turn is Now Complete")
        print()
        time.sleep(2)
        inspect()
    else:
        print()
        print("You Cannot Place a Piece on Top of Another One!")
        print()
        nextMove()
    
def inspect():
    global array
    global blackCapCount
    global whiteCapCount
    array = np.zeros((19, 19))
    for index,line in enumerate(moveMemory):
        if line[2] == "black":
            array[line[0]][line[1]] = 1
        elif line[2] == "white":
            array[line[0]][line[1]] = 2
    if len(moveMemory) < 4:
        pass
    else:
        if checkCapture() != False:
            for i in range(len(checkCapture())):
                for index, moves in enumerate(moveMemory):
                    if [moves[0],moves[1]] in checkCapture():
                        color = moves[2]
                        del moveMemory[index]
                        break
            if color == "white":
                whiteCapCount += len(checkCapture())
            elif color == "black":
                blackCapCount += len(checkCapture())
            draw_board()
            for line in moveMemory:
                place_piece(int(line[0]), int(line[1]), line[2])
            turtle.done()
            turtle.TurtleScreen._RUNNING=True
    
def checkWin():
    global array
    for i in range(19):
        for j in range(15):
            # Check for horizontal win
            if np.all(array[i, j:j+5] == 1):
                print("Black wins horizontally!")
                print()
                return True
            elif np.all(array[i, j:j+5] == 2):
                print("White wins horizontally!")
                print()
                return True

    for i in range(15):
        for j in range(19):
            # Check for vertical win
            if np.all(array[i:i+5, j] == 1):
                print("Black wins vertically!")
                print()
                return True
            elif np.all(array[i:i+5, j] == 2):
                print("White wins vertically!")
                print()
                return True

    for i in range(15):
        for j in range(15):
            # Check for diagonal win (top-left to bottom-right)
            if np.all(np.diag(array[i:i+5, j:j+5]) == 1):
                print("Black wins diagonally (top-left to bottom-right)!")
                print()
                return True
            elif np.all(np.diag(array[i:i+5, j:j+5]) == 2):
                print("White wins diagonally (top-left to bottom-right)!")
                print()
                return True

            # Check for diagonal win (bottom-left to top-right)
            if np.all(np.diag(np.fliplr(array[i:i+5, j:j+5])) == 1):
                print("Black wins diagonally (bottom-left to top-right)!")
                print()
                return True
            elif np.all(np.diag(np.fliplr(array[i:i+5, j:j+5])) == 2):
                print("White wins diagonally (bottom-left to top-right)!")
                print()
                return True
    return False

def checkCapture():
    global array
    locList = []
    global blackCapCount
    global whiteCapCount
    # Check for Horizontal Captures for white
    for index, row in enumerate(array):
        for rowIndex, num in enumerate(row):
            if num == 1:
                for remIndex, rem in enumerate(row[rowIndex+1:]):
                    if rem == 1:
                        originalIndex = rowIndex + remIndex + 1
                        if np.all(np.array(row[rowIndex+1:originalIndex]) == 2) and originalIndex - rowIndex > 2:
                            #print(f"Left Piece is ({index}, {rowIndex})")
                            #print(f"Right Piece is ({index}, {originalIndex})")
                            captured = np.array(row[rowIndex+1:originalIndex])
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for i in range(1, len(captured)+1):
                                #print(f"({index}, {rowIndex+i})")
                                locList.append([index, rowIndex+i])
    # Check for Horizontal Captures for black
    for index, row in enumerate(array):
        for rowIndex, num in enumerate(row):
            if num == 2:
                for remIndex, rem in enumerate(row[rowIndex+1:]):
                    if rem == 2:
                        originalIndex = rowIndex + remIndex + 1
                        if np.all(np.array(row[rowIndex+1:originalIndex]) == 1) and originalIndex - rowIndex > 2:
                            #print(f"Left Piece is ({index}, {rowIndex})")
                            #print(f"Right Piece is ({index}, {originalIndex})")
                            captured = np.array(row[rowIndex+1:originalIndex])
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for i in range(1, len(captured)+1):
                                #print(f"({index}, {rowIndex+i})")
                                locList.append([index, rowIndex+i]) 
    # Check for Vertical Captures for white
    for colIndex in range(array.shape[1]):
        for rowIndex, num in enumerate(array[:, colIndex]):
            if num == 1:
                for remIndex, rem in enumerate(array[rowIndex+1:, colIndex]):
                    if rem == 1:
                        originalIndex = rowIndex + remIndex + 1
                        if np.all(np.array(array[rowIndex+1:originalIndex, colIndex]) == 2) and originalIndex - rowIndex > 2:
                            #print(f"Top Piece is ({rowIndex}, {colIndex})")
                            #print(f"Bottom Piece is ({originalIndex}, {colIndex})")
                            captured = np.array(array[rowIndex+1:originalIndex, colIndex])
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for i in range(1, len(captured)+1):
                                #print(f"({rowIndex+i}, {colIndex})")
                                locList.append([rowIndex+i, colIndex])
    # Check for Vertical Captures for black
    for colIndex in range(array.shape[1]):
        for rowIndex, num in enumerate(array[:, colIndex]):
            if num == 2:
                for remIndex, rem in enumerate(array[rowIndex+1:, colIndex]):
                    if rem == 2:
                        originalIndex = rowIndex + remIndex + 1
                        if np.all(np.array(array[rowIndex+1:originalIndex, colIndex]) == 1) and originalIndex - rowIndex > 2:
                            #print(f"Top Piece is ({rowIndex}, {colIndex})")
                            #print(f"Bottom Piece is ({originalIndex}, {colIndex})")
                            captured = np.array(array[rowIndex+1:originalIndex, colIndex])
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for i in range(1, len(captured)+1):
                                #print(f"({rowIndex+i}, {colIndex})")
                                locList.append([rowIndex+i, colIndex])

    # Check for Diagonal Captures for black
    for rowIndex in range(array.shape[0]):
        for colIndex in range(array.shape[1]):
            if array[rowIndex, colIndex] == 2:
                # Upward Diagonal
                for i in range(1, min(rowIndex, colIndex) + 1):
                    if rowIndex - i >= 0 and colIndex - i >= 0 and array[rowIndex - i, colIndex - i] == 2:
                        originalIndex = rowIndex - i
                        if np.all(array[originalIndex + 1:rowIndex, colIndex - i + 1:colIndex] == 1) and rowIndex - originalIndex > 2:
                            #print(f"Upward Left Piece is ({rowIndex}, {colIndex})")
                            #print(f"Upward Right Piece is ({originalIndex}, {colIndex - i})")
                            captured = array[originalIndex + 1:rowIndex, colIndex - i + 1:colIndex]
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for j in range(1, len(captured) + 1):
                                print(f"({rowIndex - j}, {colIndex - j})")
                                locList.append([rowIndex - j, colIndex - j])
    
                # Downward Diagonal
                for i in range(1, min(array.shape[0] - rowIndex, array.shape[1] - colIndex) + 1):
                    if rowIndex + i < array.shape[0] and colIndex + i < array.shape[1] and array[rowIndex + i, colIndex + i] == 2:
                        originalIndex = rowIndex + i
                        if np.all(array[rowIndex + 1:originalIndex + 1, colIndex + 1:colIndex + i + 1] == 1) and originalIndex - rowIndex > 2:
                            #print(f"Downward Left Piece is ({rowIndex}, {colIndex})")
                            #print(f"Downward Right Piece is ({originalIndex}, {colIndex + i})")
                            captured = array[rowIndex + 1:originalIndex + 1, colIndex + 1:colIndex + i + 1]
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for j in range(1, len(captured) + 1):
                                #print(f"({rowIndex + j}, {colIndex + j})")
                                locList.append([rowIndex + j, colIndex + j])
    
    # Check for Diagonal Captures for white
    for rowIndex in range(array.shape[0]):
        for colIndex in range(array.shape[1]):
            if array[rowIndex, colIndex] == 1:
                # Upward Diagonal
                for i in range(1, min(rowIndex, array.shape[1] - colIndex) + 1):
                    if rowIndex - i >= 0 and colIndex + i < array.shape[1] and array[rowIndex - i, colIndex + i] == 1:
                        originalIndex = rowIndex - i
                        if np.all(array[originalIndex + 1:rowIndex, colIndex + i - 1:colIndex] == 2) and rowIndex - originalIndex > 2:
                            #print(f"Upward Left Piece is ({rowIndex}, {colIndex})")
                            #print(f"Upward Right Piece is ({originalIndex}, {colIndex + i})")
                            captured = array[originalIndex + 1:rowIndex, colIndex + i - 1:colIndex]
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for j in range(1, len(captured) + 1):
                                #print(f"({rowIndex - j}, {colIndex + j})")
                                locList.append([rowIndex - j, colIndex + j])
    
                # Downward Diagonal
                for i in range(1, min(array.shape[0] - rowIndex, colIndex) + 1):
                    if rowIndex + i < array.shape[0] and colIndex - i >= 0 and array[rowIndex + i, colIndex - i] == 1:
                        originalIndex = rowIndex + i
                        if np.all(array[rowIndex + 1:originalIndex + 1, colIndex - i + 1:colIndex] == 2) and originalIndex - rowIndex > 2:
                            #print(f"Downward Left Piece is ({rowIndex}, {colIndex})")
                            #print(f"Downward Right Piece is ({originalIndex}, {colIndex - i})")
                            captured = array[rowIndex + 1:originalIndex + 1, colIndex - i + 1:colIndex]
                            #print("This is captured", captured)
                            #print("Location for captured pieces are:")
                            for j in range(1, len(captured) + 1):
                                #print(f"({rowIndex + j}, {colIndex - j})")
                                locList.append([rowIndex + j, colIndex - j])
    
    return locList if locList else False
################################MAIN()#################################
menu()
option = int(input("Enter a number for options 1-5: "))
while option != 5:
    if option == 1:
        readInstructions()
    elif option == 2:
        newGame()
    elif option == 3:
        captured()
    elif option == 4 and len(moveMemory) == 0:
        print()
        print("Please Start a New Game First!")
        print()
        time.sleep(2)
    elif option == 4 and len(moveMemory) != 0:
        nextMove()
    else:
        print("Please enter a valid number from 1-5!")
    if isActive and checkWin():
        break
    menu()
    option = int(input("Enter a number for options 1-5: "))
    print()
print("Thank You for Playing!")

        
    