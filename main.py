import os
import random
import time

empty_board = [" " for x in range(9)]
board = empty_board


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def draw_board():
    table = f"""
+---+---+---+
| {board[0]} | {board[1]} | {board[2]} |
+---+---+---+
| {board[3]} | {board[4]} | {board[5]} |
+---+---+---+
| {board[6]} | {board[7]} | {board[8]} |
+---+---+---+
"""
    print(table)


def draw(field, operation, admin=False):
    if operation not in ["x", "o", " "]:
        print("invalid operation")
    else:
        if board[field] == " " or admin == True:
            board[field] = operation


def clear_board():
    for x in range(9):
        draw(x, " ", admin=True)


def try_get_int(input):
    try:
        return int(input)
    except ValueError:
        print("not a number")
    except:
        print("something else went wrong")


win_list = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def check_win(player):
    mark_list = []

    if player in ["o", "x"]:
        if " " in board:
            for x in range(9):
                if board[x] == player:
                    mark_list.append(x)

            for x in win_list:
                if all(item in mark_list for item in x):
                    clear_console()
                    draw_board()
                    print(f"{player} won!")
                    return "end"
        else:
            clear_console()
            draw_board()
            print("draw!")
            return "end"


def easy_ai_guess(player):
    try_guess_list = []

    if board[4] == " ":
        draw(4, player)
        return

    for n in range(20):
        turn = random.randrange(9)

        if turn not in try_guess_list:
            try_guess_list.append(turn)
            if board[turn] == " ":
                draw(turn, player)
                break


def get_conter(list):
    if list == [0, 1]:
        return 2
    if list == [3, 4]:
        return 5
    if list == [6, 7]:
        return 8
    if list == [0, 3]:
        return 6
    if list == [1, 4]:
        return 7
    if list == [2, 5]:
        return 8
    if list == [0, 4]:
        return 8
    if list == [2, 4]:
        return 6
    if list == [0, 2]:
        return 1
    if list == [3, 5]:
        return 4
    if list == [6, 8]:
        return 7
    if list == [0, 6]:
        return 3
    if list == [1, 7]:
        return 4
    if list == [2, 8]:
        return 5
    if list == [0, 8]:
        return 4
    if list == [2, 6]:
        return 4
    if list == [1, 2]:
        return 0
    if list == [4, 5]:
        return 3
    if list == [7, 8]:
        return 6
    if list == [3, 6]:
        return 0
    if list == [4, 7]:
        return 1
    if list == [5, 8]:
        return 2
    if list == [4, 8]:
        return 0
    if list == [4, 6]:
        return 2


conter_list = [
    [0, 1],
    [3, 4],
    [6, 7],
    [0, 3],
    [1, 4],
    [2, 5],
    [0, 4],
    [2, 4],
    [0, 2],
    [3, 5],
    [6, 8],
    [0, 6],
    [1, 7],
    [2, 8],
    [0, 8],
    [2, 6],
    [1, 2],
    [4, 5],
    [7, 8],
    [3, 6],
    [4, 7],
    [5, 8],
    [4, 8],
    [4, 6]
]


def ai_guess(player):
    op_mark_list = []
    mark_list = []

    if player == "x":
        opponent = "o"
    if player == "o":
        opponent = "x"

    if player in ["o", "x"]:
        # Get Marks
        # Opponent:
        for x in range(9):
            if board[x] == opponent:
                op_mark_list.append(x)
        
        # AI:
            for x in range(9):
                if board[x] == player:
                    mark_list.append(x)


        # Do Conter to Opponents Plays
        for x in conter_list:
            if all(item in op_mark_list for item in x):
                if board[get_conter(x)] == " ":
                    draw(get_conter(x), player)
                    return

        # Try win own move
        for x in conter_list:
            if all(item in mark_list for item in x):
                if board[get_conter(x)] == " ":
                    draw(get_conter(x), player)
                    return
        
        
        # If there's nothing to conter and didn't win yet, do random move
        easy_ai_guess(player)


def multiplayer():
    clear_board()
    clear_console()
    draw_board()

    while True:
        x_turn = input("Where to x: ")
        x_turn = try_get_int(x_turn)
        if x_turn in range(9):
            draw(x_turn, "x")

        if check_win("x") == "end":
            return

        clear_console()
        draw_board()

        o_turn = input("Where to o: ")
        o_turn = try_get_int(o_turn)
        if o_turn in range(9):
            draw(o_turn, "o")

        if check_win("o") == "end":
            return

        clear_console()
        draw_board()


def singleplayer():
    clear_board()
    clear_console()
    draw_board()
    while True:
        x_turn = input("Where to x: ")
        x_turn = try_get_int(x_turn)
        if x_turn in range(9):
            draw(x_turn, "x")

        if check_win("x") == "end":
            return

        clear_console()
        draw_board()

        ai_guess(player="o")

        if check_win("o") == "end":
            return

        clear_console()
        draw_board()

def noplayer():
    clear_board()
    clear_console()
    draw_board()
    print("This is the AI playing against itsself,\n enjoy the show!")
    while True:
        ai_guess(player="x")

        if check_win("x") == "end":
            return

        clear_console()
        draw_board()

        print("This is the AI playing against itsself,\n enjoy the show!")
        
        time.sleep(2)
        
        ai_guess(player="o")

        if check_win("o") == "end":
            return

        clear_console()
        draw_board()
        
        print("This is the AI playing against itsself,\n enjoy the show!")
        
        time.sleep(2)


def main():
    while True:
        playmode = input("Singleplayer, Multiplayer or Quit? (s/m/q)\n")
        if playmode == "m":
            multiplayer()
        elif playmode == "s":
            singleplayer()
        elif playmode == "n":
            noplayer()
        else:
            print("\n\nQuitted, thanks for playing!")
        
        


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nQuitted via Ctrl C, thanks for playing!")
