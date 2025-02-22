global c_board
global p_board


def c_board_init():
    global c_board

    c_board = [
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

def p_board_init():
    global p_board
    ships = [5, 4, 3, 3, 2]
    print(ships)

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

    place_ship(ships, 5)
    place_ship(ships, 4)
    place_ship(ships, 3)
    place_ship(ships, 2)

def place_ship(ships, a):
    valid_files = ["A","B","C","D","E","F","G","H","I","J",]
    valid_ranks = ["1","2","3","4","5","6","7","8","9","10",]

    while a in ships:
        display_board("player_only")
        print("")
        display_ships(ships)
        print("")

        x = input(f"Between which coordinates would you like to place the \"{a} ship\"? (format: \"B2 F2\")\n")
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
    if a == "player_only":
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
                if p_board[i][j]:
                    x += f" {p_board[i][j]} |"
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
                    if j == 0 and c_board[i][k]:
                        y += f" {c_board[i][k]} |"
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


c_board_init()
p_board_init()
print("")
display_board("both")