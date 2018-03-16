def printBoard(board):
    print('\n')
    print(board['tl']+' | '+board['tm']+' | '+board['tr'])
    print('---------')
    print(board['ml']+' | '+board['mm']+' | '+board['mr'])
    print('---------')
    print(board['ll']+' | '+board['lm']+' | '+board['lr'])
    print('\n')

def Winner(board):
    if board['tl']==board['tm']==board['tr']:
        if board['tl']=='X':
            return 1
        elif board['tl']=='O':
            return 2
        else:
            return 0
    elif board['ml']==board['mm']==board['mr']:
        if board['ml']=='X':
            return 1
        elif board['ml']=='O':
            return 2
        else:
            return 0
    elif board['ll']==board['lm']==board['lr']:
        if board['ll']=='X':
            return 1
        elif board['ll']=='O':
            return 2
        else:
            return 0
    elif board['tl']==board['ml']==board['ll']:
        if board['tl']=='X':
            return 1
        elif  board['tl']=='O':
            return 2
        else:
            return 0
    elif board['tm']==board['mm']==board['lm']:
        if board['tm']=='X':
            return 1
        elif board['tm']=='O':
            return 2
        else:
            return 0
    elif board['tr']==board['mr']==board['lr']:
        if board['tr']=='X':
            return 1
        elif board['tr']=='O':
            return 2
        else:
            return 0
    elif board['tl']==board['mm']==board['lr']:
        if board['tl']=='X':
            return 1
        elif board['tl']=='O':
            return 2
        else:
            return 0
    elif board['tr']==board['mm']==board['ll']:
        if board['tr']=='X':
            return 1
        elif board['tr']=='O':
            return 2
        else:
            return 0
    else:
        return 0

        
theBoard={'tl':' ', 'tm':' ','tr':' ',
          'ml':' ','mm':' ','mr':' ',
          'll':' ','lm':' ','lr':' '}
printBoard(theBoard)

currMove='X'

for i in range(9):
    print("Turn "+str(i+1)+". The current move is "+currMove+". What position?: ")
    pos=input()
    while(theBoard[pos]!=' '):
        print("wrong move... try again!")
        pos=input("What position?")
    theBoard[pos]=currMove
    if currMove=='X':
        currMove='O'
    else:
        currMove='X'
    if Winner(theBoard)>0:
        if Winner(theBoard)==1:
            print('X has won')
        else:
            print('O has won')
        break
    printBoard(theBoard)

print("Final Board: \n")
printBoard(theBoard)

input()
