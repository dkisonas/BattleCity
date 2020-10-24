import msvcrt


class GameRules:
	def __init__(self, game_level):
		self.game_level = game_level
		self.game_over = False

	def process_user_input(self):
		controls = {b'a': self.move_left, b's': self.move_down, b'd': self.move_right, b'w': self.move_up, b'q': self.set_game_over}
		controls[msvcrt.getch()]()

	def move_left(self):
		if self.game_level.game_map.is_empty_space(pos=self.game_level.tank.position.left()):
			self.game_level.tank.position = self.game_level.tank.position.left()

	def move_down(self):
		if self.game_level.game_map.is_empty_space(pos=self.game_level.tank.position.down()):
			self.game_level.tank.position = self.game_level.tank.position.down()

	def move_right(self):
		if self.game_level.game_map.is_empty_space(pos=self.game_level.tank.position.right()):
			self.game_level.tank.position = self.game_level.tank.position.right()

	def move_up(self):
		if self.game_level.game_map.is_empty_space(pos=self.game_level.tank.position.up()):
			self.game_level.tank.position = self.game_level.tank.position.up()

	def set_game_over(self):
		self.game_over = True

	def is_game_over(self):
		return self.game_over
