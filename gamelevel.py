class GameLevel:
	def __init__(self, game_map, tank, enemy_tanks):
		self.game_map = game_map
		self.player_tank = tank
		self.enemy_tanks = enemy_tanks
		self.projectiles = []

	def delete_enemy_tank_if_shot(self, projectile_pos):
		for tank in self.enemy_tanks:
			if projectile_pos == tank.position:
				self.enemy_tanks.remove(tank)
				return True

	def is_enemy_tank_at_position(self, pos):
		for tank in self.enemy_tanks:
			if pos == tank.position:
				return True

	def is_player_tank_at_position(self, pos):
		return pos == self.player_tank.position
