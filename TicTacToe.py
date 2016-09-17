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
			if winCond(theBoard) == True:
				hasWon = True
		else:
			break
		
		# AI
		while movesLeft >= 1 and hasWon == False:
			pcMove = random.randint(0,7)
			if theBoard[moves[pcMove]] == ' ':
				theBoard[moves[pcMove]] = 'O'
				movesLeft -= 1
				hasWon = True

			else:
				break


def winCond(board):

	#TOP ROW
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
	#MIDDLE ROW
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
	#BOTTOM ROW
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
	#Dia L
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

	#Dia R
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

	#Down L
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

	#Down M
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

	#Down L
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


play()