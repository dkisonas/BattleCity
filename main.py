from renderer import render_map, render_projectiles
from map import GameMap
from tank import Tank
from gamelevel import GameLevel
from position import Position
from gamerules import GameRules

game_map = GameMap()
player_tank = Tank(Position(10, 10))
game_level = GameLevel(game_map, player_tank)
game_rules = GameRules(game_level)

while not game_rules.game_over:
	render_map(game_level)
	game_rules.process_user_input()
	if len(game_level.projectiles) > 0:
		render_projectiles(game_level)
