# Tic Tac Toe Tuk

import random

def displayInstruct():
    '''Display game instructions.'''  
    print(
    '''
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe-Tuk.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number, 1 - 16.  The number 
    will correspond to the board position as illustrated:

                    13| 14| 15| 16
                    --------------
                    9 | 10| 11| 12
                    --------------
                    5 | 6 | 7 | 8
                    --------------
                    1 | 2 | 3 | 4

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    '''
    )

def drawBoard(board):
    print('   |   |   |')
    print(' ' + board[13] + ' | ' + board[14] + ' | ' + board[15] + ' | ' + board[16])
    print('   |   |   |')
    print('---------------')
    print('   |   |')
    print(' ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ' + board[12])
    print('   |   |   |')
    print('---------------')
    print('   |   |   |')
    print(' ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |   |')
    print('---------------')
    print('   |   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4])
    print('   |   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or
            (bo[5] == le and bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or
            (bo[13] == le and bo[14] == le and bo[15] == le and bo[16] == le) or
            (bo[13] == le and bo[9] == le and bo[5] == le and bo[1] == le) or
            (bo[14] == le and bo[10] == le and bo[6] == le and bo[2] == le) or
            (bo[15] == le and bo[11] == le and bo[7] == le and bo[3] == le) or
            (bo[16] == le and bo[12] == le and bo[8] == le and bo[4] == le) or
            (bo[16] == le and bo[11] == le and bo[6] == le and bo[1] == le) or
            (bo[13] == le and bo[10] == le and bo[7] == le and bo[4] == le))

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-16)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []

    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 4, 13, 16])
    if move != None:
        return move

    move = chooseRandomMoveFromList(board, [10, 11, 6, 7])
    if move != None:
        return move

    return chooseRandomMoveFromList(board, [2, 3, 5, 8, 9, 12, 14, 15])

def isBoardFull(board):
    for i in range(1, 17):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe Tuk!')

while True:
    displayInstruct()
    theBoard = [' '] * 17
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'computer'
                    
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard,computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You loose!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
