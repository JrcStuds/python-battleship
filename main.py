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

    while ships:
        display_board("p_board")
        print("")
        display_ships(ships)
        print("")

        x = input("Which ship would you like to place? (number between 2-5)\n")
        if x.isdigit():
            if int(x) in ships:
                p_place_ship(ships, int(x))
            else: print("That ship isn't available")
        else: print("That ship isn't available")
        print("")

def p_place_ship(ships, ship_num):
    # create list of valid inputs for coords
    valid_files = ["A","B","C","D","E","F","G","H","I","J",]
    valid_ranks = []
    for i in range(10): valid_ranks.append(str(i + 1))
    # toggle for coord check
    valid_coord = False
    # first and second coords
    x1 = ""
    x2 = ""

    # ask for coords until valid
    while valid_coord == False:
        display_board("p_board")
        print("")
        display_ships(ships)
        print("")

        valid_coord = True
        # input
        raw_coords = input(f"Between which coordinates would you like to place the \"{ship_num} ship\"? (format: \"B2 F2\")\n")

        # check length of string, only one space, both to avoid errors
        if len(raw_coords) >= 5 and len(raw_coords) <= 7 and raw_coords.count(" ") == 1:
            # create temporary first and second coord values to test, coords with 10
            # no 10 coord
            if raw_coords.index(" ") == 2 and len(raw_coords) == 5:
                x1 = [raw_coords[0], raw_coords[1]]
                x2 = [raw_coords[3], raw_coords[4]]
            # if 10 coord in first coord
            elif raw_coords.index(" ") == 3 and len(raw_coords) == 6:
                x1 = [raw_coords[0], raw_coords[1:3]]
                x2 = [raw_coords[4], raw_coords[5]]
            # if 10 coord in second coord
            elif raw_coords.index(" ") == 2 and len(raw_coords) == 6:
                x1 = [raw_coords[0], raw_coords[1]]
                x2 = [raw_coords[3], raw_coords[4:6]]
            # if both coords have 10
            elif raw_coords.index(" ") == 3 and len(raw_coords) == 7:
                x1 = [raw_coords[0], raw_coords[1:3]]
                x2 = [raw_coords[4], raw_coords[5:7]]
            else: valid_coord = False
            
            # last check of coord formatting
            if valid_coord == True:
                # if the first characters of each coord are not valid letters
                if x1[0] not in valid_files or x2[0] not in valid_files:
                    valid_coord = False
                    print("Those aren't valid coordinates")
                # if the second characters of each coord are not valid numbers
                elif x1[1] not in valid_ranks or x2[1] not in valid_ranks:
                    valid_coord = False
                    print("Those aren't valid coordinates")

                # now checking the actual spacing of the coordinates
                # NOT if only the x has changed or only the y has changed
                elif not ((coord(x1)[0] == coord(x2)[0]) ^ (coord(x1)[1] == coord(x2)[1])):
                    valid_coord = False
                    print("Those coordinates aren't in a line")
                # if the coordinates aren't 5 spaces apart
                elif not (abs(coord(x1)[0] - coord(x2)[0]) == (ship_num-1) or abs(coord(x1)[1] - coord(x2)[1]) == (ship_num-1)):
                    valid_coord = False
                    print(f"Those spaces aren't {ship_num} apart")
                
                # now actually write the ship in if all fail checks pass
                else:
                    # remove ship from ships
                    ships.remove(ship_num)

                    # up
                    if coord(x1)[1] < coord(x2)[1]:
                        for i in range(ship_num):
                            p_board[coord(x1)[1] + i][coord(x1)[0]] = ship_num
                    # down
                    elif coord(x1)[1] > coord(x2)[1]:
                        for i in range(ship_num):
                            p_board[coord(x1)[1] - i][coord(x1)[0]] = ship_num
                    # left
                    elif coord(x1)[0] > coord(x2)[0]:
                        for i in range(ship_num):
                            p_board[coord(x1)[1]][coord(x1)[0] - i] = ship_num
                    # right
                    elif coord(x1)[0] < coord(x2)[0]:
                        for i in range(ship_num):
                            p_board[coord(x1)[1]][coord(x1)[0] + i] = ship_num
        else:
            valid_coord = False
            print("Invalid coordinate format")

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
    
    print("")

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
display_board("both")
display_board("o_board_hidden")