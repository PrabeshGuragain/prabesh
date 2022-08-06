#from input import *
import random
import shutil
columns = shutil.get_terminal_size().columns
board = ['-','-','-','-','-','-','-','-','-']
turn = 'X'
'''def Display_board():
    print(f'{board[0]} | {board[1]} | {board[2]}    1 | 2 | 3'.center(columns))
    print(f'{board[3]} | {board[4]} | {board[5]}    4 | 5 | 6'.center(columns))    
    print(f'{board[6]} | {board[7]} | {board[8]}    1 | 2 | 3'.center(columns)) '''   

def Display_board():
    print(board[0] + '|' + board[1] + '|'+ board[2]+'        1 | 2 | 3')
    print(board[3] + '|' + board[4] + '|'+ board[5]+'        4 | 5 | 6')
    print(board[6] + '|' + board[7] + '|'+ board[8]+'        7 | 8 | 9')

def switchTurn(a):
    global turn
    if  a == 'X':
        turn = 'O' 
    elif a == 'O':
        turn = 'X'

def CheckWin(board):
    bvalue = BoardValue(board)
    # rows
    a = bvalue[0] + bvalue[1] + bvalue[2]
    b = bvalue[3] + bvalue[4] + bvalue[5]
    c = bvalue[6] + bvalue[7] + bvalue[8]
    # colums
    d = bvalue[0] + bvalue[3] + bvalue[6]
    e = bvalue[4] + bvalue[1] + bvalue[7]
    f = bvalue[8] + bvalue[5] + bvalue[2]
    # diagonals
    g = bvalue[0] + bvalue[4] + bvalue[8]
    h = bvalue[6] + bvalue[4] + bvalue[2]

    if -3 in [a,b,c,d,e,f,g,h]: 
        return True
    elif 3 in [a,b,c,d,e,f,g,h]: 
        return True
    return False

def BoardValue(board):
    bvalue= [0,0,0,
            0,0,0,
            0,0,0]
    for i in range(9):
        a = board[i]
        if a == 'X':
            bvalue[i] = -1
        elif a == 'O':
            bvalue[i] = 1
    return bvalue

def RandomComputerInput(board):
    R = []
    for i in range(len(board)):
        if board[i] == '-':
            R.append(i)
    
    return R[random.randint(0,len(R))-1]

def UserInput(board):
    position = int(input("Choose un-occupied position: ")) - 1
    while board[position] != '-':
        print('The place is already occupied. Please selcet another place.')
        position = int(input("Enter position between 1-9: ")) - 1
    return position

def ChangeBoard(board,position,turn):
    board[position] = turn
    return board

print('Tic Tac Toe: Human Vs Random Computer'.center(columns))

for i in range(9):
    Display_board()
    if turn == 'X':
        position = UserInput(board)
    elif turn == 'O':
        position = RandomComputerInput(board)
    ChangeBoard(board,position,turn)
    if CheckWin(board):
        print()
        Display_board()
        print(f'{turn} won!'.center(columns))
        print('Game Over!!'.center(columns))
        break
    switchTurn(turn)
    print()
else:
    Display_board()
    print("It's a tie!")

input('This is still in a development phase so please privide your feedback: ')
# Natak Nai Ho. Feedback store hudaina.
print('-----------------Thanks for playing------------------------------------')
print('Develpoed by Prabesh Guragain.')
input()
