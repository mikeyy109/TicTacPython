theBoard = {'t_l':' ', 't_m':' ', 't_r':' ',
            'm_l':' ', 'm_m':' ', 'm_r':' ',
            'b_l':' ', 'b_m':' ', 'b_r':' '}

def printBoard(board):
	print(board['t_l'] + '|' + board['t_m'] + '|' + board['t_r'])
	print('-+-+-')
	print(board['m_l'] + '|' + board['m_m'] + '|' + board['m_r'])
	print('-+-+-')
	print(board['b_l'] + '|' + board['b_m'] + '|' + board['b_r'])


printBoard(theBoard)