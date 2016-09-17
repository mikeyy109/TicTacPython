import random

theBoard = {'t_l':' ', 't_m':' ', 't_r':' ',
            'm_l':' ', 'm_m':' ', 'm_r':' ',
            'b_l':' ', 'b_m':' ', 'b_r':' '}

moves = ['t_l', 't_m', 't_r', 'm_l', 'm_m', 'm_r', 'b_l', 'b_m', 'b_r']

def printBoard(board):
	print('You are \'X\'\n')
	print(board['t_l'] + '|' + board['t_m'] + '|' + board['t_r'])
	print('-+-+-')
	print(board['m_l'] + '|' + board['m_m'] + '|' + board['m_r'])
	print('-+-+-')
	print(board['b_l'] + '|' + board['b_m'] + '|' + board['b_r'])
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
		else:
			break
		
		# AI
		while movesLeft >= 1 and hasWon == False:
			pcMove = random.randint(0,7)
			if theBoard[moves[pcMove]] == ' ':
				theBoard[moves[pcMove]] = 'O'
				movesLeft -= 1
				break

printBoard(theBoard)