from renderer import render_map, render_projectiles
from map import GameMap
from tank import PlayerTank, EnemyTank
from gamelevel import GameLevel
from position import Position
from gamerules import GameRules

game_map = GameMap()
player_tank = PlayerTank(Position(10, 10))
enemy_tanks = [EnemyTank(Position(10, 1)), EnemyTank(Position(13, 1))]
game_level = GameLevel(game_map, player_tank, enemy_tanks)
game_rules = GameRules(game_level)

while not game_rules.game_over:
	render_map(game_level)
	game_rules.process_user_input()
	if len(game_level.projectiles) > 0:
		render_projectiles(game_level)
