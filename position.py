class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def at(self, x, y):
		return self.x == x and self.y == y

	def left(self):
		return Position(self.x-1, self.y)

	def right(self):
		return Position(self.x+1, self.y)

	def up(self):
		return Position(self.x, self.y-1)

	def down(self):
		return Position(self.x, self.y+1)
