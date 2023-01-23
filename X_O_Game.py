#game made by me taken from a bronze ww main
import time
import random
def printboard():
    global board;
    board=[" " for i in range(9)]
    x= "|=================|"
    ol="|     |     |     |"
    row1="|  {}  |  {}  |  {}  |".format(board[0],board[1],board[2])
    row2="|  {}  |  {}  |  {}  |".format(board[3],board[4],board[5])
    row3="|  {}  |  {}  |  {}  |".format(board[6],board[7],board[8])
    print(x);
    print(ol)
    print(row1)
    print(ol)
    print(x)
    print(ol)
    print(row2)
    print(ol)
    print(x)
    print(ol)
    print(row3)
    print(ol)
    print(x)
def who(c,name1,name2):
        print("{} You want (X) or (O)? ".format(name1))
        v1=input()
        v2="0";
        if v1=="x" or v1=="X": v2 ="O";
        elif v1=="o" or v1=="O": v2="X";
        else:
            if(c<4):print("Choose x or o ... Try again"); 
            time.sleep(1)
            if(c<4):print("So Again{}".format("!"*c))
            time.sleep(0.5) 
            c=c+1
            if(c==5):
                print("Get lost")
                time.sleep(3)
                print("idiot")
                exit()
            who(c,name1,name2);
        print("player {name1} Has ({v1}) player {name2} Has ({v2})".format(v1,name1,v2,name2));
        return [v1,v2];
def playermove(name1,name2,v1,v2):
    # print("{} Enter your move(X/O):".format(name1))
    # icon=input();
    # number=0;
    # print()
    # if icon=="x" or icon=="X": number =1;
    # elif icon=="o" or icon=="O": number=2;
    # else:
    #     print("Moves Are Either ({v1}) for player {name1} of ({v2}) for player {name2}"); 
    #     playermove(name1,name2,v1,v2);
    print("Your Turn {name1}".format(name1))
    choice=int(input("Enter your move(0-9): "))
    if(board[choice-1]==" "):
        board[choice-1]=v1;
    else:
        print("That space is Taken!");
        print("Try Again");
        playermove(name1,name2,v1,v2);
while(True):
    c=0;
    x=["😁","😊","😄","😃","😅","🤭","🤧","💀","🦞","🦀","🧻","🦔"]
    y=random.choice(x)
    print("Welcome To Tic Tac Toe {}".format(y))
    time.sleep(1);
    print("First Player Plays First !!")
    name1=input("First Player Name :")
    name2=input("Second Player Name :")
    printboard()
    v=who(c,name1,name2)
    playermove(name1,name2,v[0],v[1])
    printboard()
    print("Want To Play Again?")
    replay= input("y/n")
    if(replay=="n"): 
        print("❤Thanks For Playing❤")
        break;

        