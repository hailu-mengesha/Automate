#Automate the boring stuff tic-tac-toe game
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
def testWinner(board):
    won = False

    if((board['top-L'] == board['top-M'] == board['top-R']) and board['top-L'] != ' '):
        won = True
    elif(board['mid-L'] == board['mid-M'] == board['mid-R'] and board['mid-L'] != ' '):
        won = True 
    elif(board['low-L'] == board['low-M'] == board['low-R'] and board['low-M'] != ' '):
        won = True
    elif(board['top-L'] == board['mid-L'] == board['low-L'] and board['low-L'] != ' '):
        won = True
    elif(board['top-M'] == board['mid-M'] == board['low-M'] and board['low-M'] != ' '):
        won = True
    elif(board['top-R'] == board['mid-R'] == board['low-R'] and board['low-R'] != ' '):
        won = True
    elif(board['top-L'] == board['mid-M'] == board['low-R'] and board['low-R'] != ' '):
        won = True
    elif(board['top-R'] == board['mid-M'] == board['low-L'] and board['mid-R'] != ' '):
        won = True
    return won


for i in range(9):
    printBoard(theBoard)
    move = input('Turn for :' + turn + ' Move to : ')

    while not theBoard[move]== ' ':
        move = input('The space already taken,Enter another move!!')

    theBoard[move] = turn
    won = testWinner(theBoard)
    if won:
        print(turn + ' wins the game!')
        break
    elif turn == 'X':
        turn = '0'
    else:
        turn = 'X'
printBoard(theBoard)



