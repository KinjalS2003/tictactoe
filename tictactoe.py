import os
import time

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
win=1
Draw=-1
Running=0
stop=1
Game=Running
Mark='X'

def DrawBoard():
    print(" %s  | %s  | %s "%(board[1],board[2],board[3]))
    print("____|____|____")
    print(" %s  | %s  | %s "%(board[4],board[5],board[6]))
    print("____|____|____")
    print(" %s  | %s  | %s "%(board[7],board[8],board[9]))
    print("    |    |    ")


def CheckPosition(pos):
    if (board[pos]==' '):
        return True
    else:
        return False


def CheckWin():
    #Horizontal winning condition
    global Game
    if(board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
        Game=win
        return 
    elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
        Game=win
        return 
    elif(board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
        Game=win
        return  

    #vertical winning condition
    if(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        Game=win
        return  
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        Game=win
        return  
    elif(board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
        Game=win
        return  

    #Diagonal winning condition
    if(board[1]==board[5] and board[5]==board[9] and board[5]!=' '):
        Game=win
        return  
    elif(board[3]==board[5] and board[5]==board[7] and board[5]!=' '):
        Game=win
        return  

    #Match Tie or Draw Condition
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw
        return
    else:
        Game=Running

#Main Logic       
print("Tic-tac-Toe Game")
print("Player 1[X]---player 2[O]\\n")
print()
print("please wait...")
time.sleep(1)

while(Game==Running):
    os.system('cls')
    DrawBoard()
    if(player%2!=0):
        print("player 1's chance")
        Mark='X'
    else:
        print("player 2's chance")
        Mark='O'
        
    choice=int(input("Enter the position between [1-9] where you want to mark:"))
    if(CheckPosition(choice)):
        board[choice]=Mark
        player+=1
        CheckWin()

os.system('cls')
DrawBoard()
if(Game==Draw):
    print("Game Draw")
elif(Game==win):
    player-=1
    if(player%2!=0):
        print("player 1 won")
    else:
        print("player 2 won")
