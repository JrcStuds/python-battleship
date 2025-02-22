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
                x += f" {10 - 1} |"
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


c_board_init()
p_board_init()
display_board("player_only")
display_board("both")