import numpy as np

class board:
	def __init__(self):
		self.board = np.zeros(shape=(3, 3), dtype=np.uint8)
		self.currentPlayer = 1

	def __str__(self):
		mappings = {
			0: ' ',
			1: 'X',
			2: 'O'
		}
		total = []
		for y in range(self.board.shape[0]):
			row = []
			for x in range(self.board.shape[1]):
				pos = (x, y)
				self[pos] = 0
				value = self[pos]
				row.append(mappings[value])
			total.append('  ' + ' | '.join(row))
		out = '\n -----------\n'.join(total)
		return out

	def __getitem__(self, position):
		x, y = position
		return self.board[y][x]

	def __setitem__(self, position, value):
		x, y = position
		self.board[y][x] = value

	def playerMove(self, player, position):
		assert player == self.currentPlayer, f"it is not player {player}'s turn"
		targetValue = self.board[position]


if __name__ == '__main__':
	b = board()
	print(b)
