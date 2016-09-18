import random

theBoard = {'t_l': ' ', 't_m': ' ', 't_r': ' ',
            'm_l': ' ', 'm_m': ' ', 'm_r': ' ',
            'b_l': ' ', 'b_m': ' ', 'b_r': ' '}

moves = ['t_l', 't_m', 't_r', 'm_l', 'm_m', 'm_r', 'b_l', 'b_m', 'b_r']


def printBoard(board):
    print('You are \'X\'\n')
    print(board['t_l'] + '|' + board['t_m'] + '|' + board['t_r'])
    print('-+-+-')
    print(board['m_l'] + '|' + board['m_m'] + '|' + board['m_r'])
    print('-+-+-')
    print(board['b_l'] + '|'
          + board['b_m'] + '|' + board['b_r'])
    print("\n\n")


def play():
    movesLeft = 9
    hasWon = False

    # Player
    while movesLeft >= 1 and hasWon == False:
        printBoard(theBoard)
        move = str(input("Enter move: "))
        if move in moves:
            theBoard[move] = "X"
            movesLeft -= 1
            if winCond(theBoard) == True:
                hasWon = True
                gameWon()
        else:
            break

        # AI
        '''while movesLeft >= 1 and hasWon == False:
			pcMove = random.randint(0,7)
			if theBoard[moves[pcMove]] == ' ':
				theBoard[moves[pcMove]] = 'O'
				movesLeft -= 1
				if winCond(theBoard) == True:
					hasWon = True
					gameWon()
				break'''

        # AI MK2
        if movesLeft >= 1 and hasWon == False:
            moveTaken = False

            # Check for winning move
            for i in range(0, 8):
                boardCopy = theBoard
                if boardCopy[moves[i]] == ' ':
                    boardCopy[moves[i]] = 'O'
                    if winCond(boardCopy) == True:
                        theBoard[moves[i]] = 'O'
                        hasWon = True
                        gameWon()
                    else:
                        boardCopy[moves[i]] = ' '

            # Check to counter player win
            for i in range(0, 8):
                boardCopy = theBoard
                if boardCopy[moves[i]] == ' ':
                    boardCopy[moves[i]] = 'X'
                    if winCond(boardCopy) == True and moveTaken == False:
                        theBoard[moves[i]] = 'O'
                        moveTaken = True
                        break
                    else:
                        boardCopy[moves[i]] = ' '

            # Failing that. Pick a random move (For now)
            if moveTaken == False:
                pcMove = random.randint(0, 8)
                if theBoard[moves[pcMove]] == ' ':
                    theBoard[moves[pcMove]] = 'O'
                    movesLeft -= 1
                    if winCond(theBoard) == True:
                        hasWon = True
                        gameWon()
                    break


def winCond(board):
    # TOP ROW
    if board['t_l'] == board['t_m'] and board['t_m'] == board['t_r']:
        if board['t_l'] != ' ':
            if board['t_l'] == 'X':
                print('Player Wins\n')
                return True
            else:
                print('Computer Wins\n')
                return True
        else:
            return False
    # MIDDLE ROW
    if board['m_l'] == board['m_m'] and board['m_m'] == board['m_r']:
        if board['m_l'] != ' ':
            if board['m_l'] == 'X':
                print('Player Wins\n')
                return True
            else:
                print('Computer Wins\n')
                return True
        else:
            return False
    # BOTTOM ROW
    if board['b_l'] == board['b_m'] and board['b_m'] == board['b_r']:
        if board['b_l'] != ' ':
            if board['b_l'] == 'X':
                print('\nPlayer Wins\n')
                return True
            else:
                print('\nComputer Wins\n')
                return True
        else:
            return False
    # Dia L
    if board['t_l'] == board['m_m'] and board['m_m'] == board['b_r']:
        if board['t_l'] != ' ':
            if board['t_l'] == 'X':
                print('\nPlayer Wins\n')
                return True
            else:
                print('\nComputer Wins\n')
                return True
        else:
            return False

    # Dia R
    if board['t_r'] == board['m_m'] and board['m_m'] == board['b_l']:
        if board['t_r'] != ' ':
            if board['t_r'] == 'X':
                print('\nPlayer Wins\n')
                return True
            else:
                print('\nComputer Wins\n')
                return True
        else:
            return False

    # Down L
    if board['t_l'] == board['m_l'] and board['m_l'] == board['b_l']:
        if board['t_l'] != ' ':
            if board['t_l'] == 'X':
                print('\nPlayer Wins\n')
                return True
            else:
                print('\nComputer Wins\n')
                return True
        else:
            return False

    # Down M
    if board['t_m'] == board['m_m'] and board['m_m'] == board['b_m']:
        if board['t_m'] != ' ':
            if board['t_m'] == 'X':
                print('\nPlayer Wins\n')
                return True
            else:
                print('\nComputer Wins\n')
                return True
        else:
            return False

    # Down L
    if board['t_r'] == board['m_r'] and board['m_r'] == board['b_r']:
        if board['t_r'] != ' ':
            if board['t_r'] == 'X':
                print('\nPlayer Wins\n')
                return True
            else:
                print('\nComputer Wins\n')
                return True
        else:
            return False


def gameWon():
    print('#######################')
    print('###### Game Over ######')
    print('#######################')
    print('\n\nPlay Again?\n')
    ans = input('Y / N ?')
    if ans.upper() == 'Y':
        for i in theBoard:
            theBoard[i] = ' '
        play()
    elif ans.upper() == 'N':
        print('ok')
    else:
        print('Sorry i didnt get that..')


play()
