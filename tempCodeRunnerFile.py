#game made by me taken from bronze ww main
def printboard():
    global board;
    board=[" " for i in range(9)]
    x="|=====|"
    row1="|{}|{}|{}| ".format(board[0],board[1],board[2])
    row2="|{}|{}|{}| ".format(board[3],board[4],board[5])
    row3="|{}|{}|{}| ".format(board[6],board[7],board[8])
    print(x);
    print(row1)
    print(x)
    print(row2)
    print(x)
    print(row3)
    print(x)
def playermove():
    input()
    icon=input();
    number=0;
    if icon=="x" or icon=="X": number =1;
    elif icon=="o" or icon=="O": number=2;
    else:
        print("Renter your move again (X/O)"); 
        playermove();
    print("Your Turn Player {}".format(number))
    choice=int(input("Enter your move(0-9): "))
    if(board[choice-1]==" "):
        board[choice-1]=icon;
    else:
        print("That space is Taken!");
        print("Try Again");
        playermove();
while(1):
    printboard()
    playermove()
    printboard()