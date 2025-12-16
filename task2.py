board = [" "]*9

def show():
    
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def win(p):

    return ((board[0]==p and board[1]==p and board[2]==p) or
            (board[3]==p and board[4]==p and board[5]==p) or
            (board[6]==p and board[7]==p and board[8]==p) or
            (board[0]==p and board[3]==p and board[6]==p) or
            (board[1]==p and board[4]==p and board[7]==p) or
            (board[2]==p and board[5]==p and board[8]==p) or
            (board[0]==p and board[4]==p and board[8]==p) or
            (board[2]==p and board[4]==p and board[6]==p))

def ai():
    
    for i in range(9): #AI MOVE
        if board[i] == " ":
            board[i] = "O"
            if win("O"):
                return
            board[i] = " "

    for i in range(9): #HUMAN MOVE
        if board[i] == " ":
            board[i] = "X"
            if win("X"):
                board[i] = "O"
                return
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return

print("!TIC TAC TOE!")
show()

while True:
    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] != " ":
        print("Invalid move")
        continue

    board[pos] = "X"
    show()

    if win("X"):
        print("You win!")
        break

    if " " not in board:
        print("Draw")
        break

    ai()
    print("AI move:")
    show()

    if win("O"):
        print(" AI wins!")
        break
