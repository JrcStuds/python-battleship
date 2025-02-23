import random

global o_board_shown
global o_board_hidden
global p_board


def o_board_init():
    global o_board_shown
    global o_board_hidden

    o_board_shown = [
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
    ]
    o_board_hidden = [
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
    ]

    x1 = (0, 0)
    x2 = (0, 0)

    o_place_ship(5)
    o_place_ship(4)
    o_place_ship(3)
    o_place_ship(3)
    o_place_ship(2)

def p_board_init():
    global p_board
    ships = [5, 4, 3, 3, 2]

    p_board = [
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
    ]

    display_board("p_board")
    print("")
    display_ships(ships)
    print("")

    while ships:
        x = input("Which ship would you like to place? (number between 2-5)\n")
        if x.isdigit():
            if int(x) in ships:
                print(3)
            else: print(2)
        else: print(1)

def o_place_ship(a):
    x = False
    y = random.randint(0,3)
    z = []

    while x == False:
        z = []
        # up
        if y == 0:
            # pick a random place at least {a} squares from top
            l = (random.randint(0,9), random.randint(a-1,9))
            # repeat a times
            for i in range(a):
                # if square origin +/- i is empty, add to z
                if o_board_hidden[l[1] - i][l[0]] == "":
                    z.append((l[0], l[1] - i))
        # down
        elif y == 1:
            # pick a random place at least {a} squares from bottom
            l = (random.randint(0,9), random.randint(0,10-a))
            # repeat a times
            for i in range(a):
                # if square origin +/- i is empty, add to z
                if o_board_hidden[l[1] + i][l[0]] == "":
                    z.append((l[0], l[1] + i))
        # left
        elif y == 2:
            # pick a random place at least {a} squares from left
            l = (random.randint(a-1,9), random.randint(0,9))
            # repeat a times
            for i in range(a):
                # if square origin +/- i is empty, add to z
                if o_board_hidden[l[1]][l[0] - i] == "":
                    z.append((l[0] - i, l[1]))
        # right
        elif y == 3:
            # pick a random place at least {a} squares from right
            l = (random.randint(0,10-a), random.randint(0,9))
            # repeat a times
            for i in range(a):
                # if square origin +/- i is empty, add to z
                if o_board_hidden[l[1]][l[0] + i] == "":
                    z.append((l[0] + i, l[1]))

        # if all squares are empty, pass
        if len(z) == a:
            x = True
    
    for i in range(a):
        o_board_hidden[z[i][1]][z[i][0]] = a

def p_place_ship(ships, a):
    valid_files = ["A","B","C","D","E","F","G","H","I","J",]
    valid_ranks = ["1","2","3","4","5","6","7","8","9","10",]

    while a in ships:
        display_board("p_board")
        print("")
        display_ships(ships)
        print("")

        x = input(f"Between which coordinates would you like to place the \"{a} ship\"? (format: \"B2 F2\")\n")
        # check provided coords are at least 5 chars to prevent errors
        if len(x) >= 5 and len(x) <= 7 and x.count(" ") == 1:
            # first and second coordinates provided
            # if no 10 coord
            if x.index(" ") == 2 and len(x) == 5:
                y1 = [x[0], x[1]]
                y2 = [x[3], x[4]]
            # if 10 coord in first coord
            elif x.index(" ") == 3 and len(x) == 6:
                y1 = [x[0], x[1:3]]
                y2 = [x[4], x[5]]
            # if 10 coord in second coord
            elif x.index(" ") == 2 and len(x) == 6:
                y1 = [x[0], x[1]]
                y2 = [x[3], x[4:6]]
            # if both coords have 10
            elif len(x) == 7:
                y1 = [x[0], x[1:3]]
                y2 = [x[4], x[5:7]]

            # first checking coords are valid
            # if the first characters of each coord are not valid letters
            if y1[0] not in valid_files or y2[0] not in valid_files:
                print(1)
            # if the second characters of each coord are not valid numbers
            elif y1[1] not in valid_ranks or y2[1] not in valid_ranks:
                print(2)

            # now checking the actual spacing of the coordinates
            # NOT if only the x has changed or only the y has changed
            elif not ((coord(y1)[0] == coord(y2)[0]) ^ (coord(y1)[1] == coord(y2)[1])):
                print(3)
                print(f"x {coord(y1)[0] == coord(y2)[0]}  y1 {coord(y1)[0]}  y2 {coord(y2)[0]}")
                print(f"y {coord(y1)[1] == coord(y2)[1]}  y1 {coord(y1)[1]}  y2 {coord(y2)[1]}")
            # if the coordinates aren't 5 spaces apart
            elif not (abs(coord(y1)[0] - coord(y2)[0]) == (a-1) or abs(coord(y1)[1] - coord(y2)[1]) == (a-1)):
                print(4)
                print(f"x {abs(coord(y1)[0] - coord(y2)[0]) != 5} {abs(coord(y1)[0] - coord(y2)[0])}")
                print(f"y {abs(coord(y1)[1] - coord(y2)[1]) != 5} {abs(coord(y1)[1] - coord(y2)[1])}")

            # if all fail checks pass
            else:
                # remove a ship from available ships, ending loop
                ships.pop(ships.index(a))

                # now filling in board spaces
                # up
                if coord(y1)[1] < coord(y2)[1]:
                    for i in range(a):
                        p_board[coord(y1)[1] + i][coord(y1)[0]] = a
                # down
                elif coord(y1)[1] > coord(y2)[1]:
                    for i in range(a):
                        p_board[coord(y1)[1] - i][coord(y1)[0]] = a
                # left
                elif coord(y1)[0] > coord(y2)[0]:
                    for i in range(a):
                        p_board[coord(y1)[1]][coord(y1)[0] - i] = a
                # right
                elif coord(y1)[0] < coord(y2)[0]:
                    for i in range(a):
                        p_board[coord(y1)[1]][coord(y1)[0] + i] = a

def coord(x):
    # split string coordinate into list of 2 coordinates (x, y)
    y = [x[0], x[1]]

    # for x coordinate, convert letter into number (0 is left, 9 is right)
    if y[0] == "A":
        y[0] = 0
    elif y[0] == "B":
        y[0] = 1
    elif y[0] == "C":
        y[0] = 2
    elif y[0] == "D":
        y[0] = 3
    elif y[0] == "E":
        y[0] = 4
    elif y[0] == "F":
        y[0] = 5
    elif y[0] == "G":
        y[0] = 6
    elif y[0] == "H":
        y[0] = 7
    elif y[0] == "I":
        y[0] = 8
    elif y[0] == "J":
        y[0] = 9
    
    # for y coordinate, top is 0
    y[1] = 10 - int(y[1])

    return (y[0], y[1])

def display_board(a):
    if a == "p_board":
        header = "                  YOUR BOARD"
        letters = "     A   B   C   D   E   F   G   H   I   J"
        line = "   +---+---+---+---+---+---+---+---+---+---+"

        print(header)
        print(letters)
        print(line)

        # repeat 10 times for 10 rows (y coord)
        for i in range(10):
            # variable for row
            x = ""
            # add row number at start of row
            if i == 0:
                x += f"{10 - i} |"
            else:
                x += f" {10 - i} |"
            # repeat 10 times for 10 cells (x coord)
            for j in range(10):
                if type(p_board[i][j]) == int:
                    x += f" {bold(p_board[i][j])} |"
                elif p_board[i][j]:
                    x += f" {p_board[i][j]} |"
                else:
                    x += "   |"
            # add row number at end of row
            x += f" {10 - i}"
            # print row and separating line
            print(x)
            print(line)
        
        print(letters)

    elif a == "o_board_shown":
        header = "                OPPONENT'S BOARD"
        letters = "     A   B   C   D   E   F   G   H   I   J"
        line = "   +---+---+---+---+---+---+---+---+---+---+"

        print(header)
        print(letters)
        print(line)

        # repeat 10 times for 10 rows (y coord)
        for i in range(10):
            # variable for row
            x = ""
            # add row number at start of row
            if i == 0:
                x += f"{10 - i} |"
            else:
                x += f" {10 - i} |"
            # repeat 10 times for 10 cells (x coord)
            for j in range(10):
                if type(o_board_shown[i][j]) == int:
                    x += f" {bold(o_board_shown[i][j])} |"
                elif o_board_shown[i][j]:
                    x += f" {o_board_shown[i][j]} |"
                else:
                    x += "   |"
            # add row number at end of row
            x += f" {10 - i}"
            # print row and separating line
            print(x)
            print(line)
        
        print(letters)

    elif a == "o_board_hidden":
        header = "                OPPONENT'S BOARD"
        letters = "     A   B   C   D   E   F   G   H   I   J"
        line = "   +---+---+---+---+---+---+---+---+---+---+"

        print(header)
        print(letters)
        print(line)

        # repeat 10 times for 10 rows (y coord)
        for i in range(10):
            # variable for row
            x = ""
            # add row number at start of row
            if i == 0:
                x += f"{10 - i} |"
            else:
                x += f" {10 - i} |"
            # repeat 10 times for 10 cells (x coord)
            for j in range(10):
                if type(o_board_hidden[i][j]) == int:
                    x += f" {bold(o_board_hidden[i][j])} |"
                elif o_board_hidden[i][j]:
                    x += f" {o_board_hidden[i][j]} |"
                else:
                    x += "   |"
            # add row number at end of row
            x += f" {10 - i}"
            # print row and separating line
            print(x)
            print(line)
        
        print(letters)

    elif a == "both":
        headers = "               OPPONENT'S BOARD                                         YOUR BOARD"
        letters = "     A   B   C   D   E   F   G   H   I   J                 A   B   C   D   E   F   G   H   I   J"
        line = "   +---+---+---+---+---+---+---+---+---+---+             +---+---+---+---+---+---+---+---+---+---+"

        print(headers)
        print(letters)
        
        print(line)
        # repeat 10 times for 10 rows (y coord)
        for i in range(10):
            # variable for row
            x = ""
            # repeat 2 times for 2 boards
            for j in range(2):
                # variable for row of board
                y = ""
                # add total row number at start of board row
                if i == 0:
                    y += f"{10 - i} |"
                else:
                    y += f" {10 - i} |"
                # repeat 10 times for 10 cells (x coord)
                for k in range(10):
                    # check which board data should come from
                    if j == 0 and type(o_board_shown[i][k]) == int:
                        y += f" {o_board_shown[i][k]} |"
                    elif j == 0 and o_board_shown[i][k]:
                        y += f" {o_board_shown[i][k]} |"
                    elif j == 1 and type(p_board[i][k]) == int:
                        y += f" {p_board[i][k]} |"
                    elif j == 1 and p_board[i][k]:
                        y += f" {p_board[i][k]} |"
                    else:
                        y += "   |"
                # add row number at end of board row
                if i == 0:
                    y += f" {10 - i}"
                else:
                    y += f" {10 - i} "
                # add board row to total row
                x += f"{y}       "
            # print row and separating line
            print(x)
            print(line)
        
        print(letters)

def display_ships(a):
    b = []
    for i in range(len(a)):
        b.append(a[i])

    # string for printing
    x1 = ""
    x2 = ""
    x3 = ""
    x4 = ""

    if 5 in b:
        x1 += "   /-----5-----\\"
        x2 += "   \\-----------/"
        b.pop(b.index(5))
    
    if 4 in b:
        x1 += "   /----4----\\"
        x2 += "   \\---------/"
        b.pop(b.index(4))

    for i in range(2):
        if 3 in b:
            x3 += "   /---3---\\"
            x4 += "   \\-------/"
            b.pop(b.index(3))
    
    if 2 in b:
        x3 += "   /--2--\\"
        x4 += "   \\-----/"
        b.pop(b.index(2))
    
    print("SHIPS AVAILABLE:\n")
    if x1:
        print(x1)
        print(x2)
        print("")
    print(x3)
    print(x4)

def bold(x):
    return "\033[1m" + str(x) + "\033[0m"


o_board_init()
p_board_init()
print("")
display_board("both")
display_board("o_board_hidden")