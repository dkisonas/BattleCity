import random

# msvcrt.getch()
from position import Position
from projectile import Projectile


class GameRules:
    def __init__(self, game_level):
        self.game_level = game_level
        self.game_over = False

    def process_user_input(self):
        controls = {'a': self.move_left,
                    's': self.move_down,
                    'd': self.move_right,
                    'w': self.move_up,
                    'q': self.set_game_over,
                    'k': self.shoot_projectile}
        key = input()
        if key in 'wasdk':
            controls[key](tank=self.game_level.player_tank)
        else:
            controls[key]()

    def move_left(self, tank):
        if self.game_level.game_map.is_empty_space(pos=tank.position.left())\
                and not self.game_level.is_enemy_tank_at_position(tank.position.left()):
            tank.position = tank.position.left()
            tank.turn_left()
        elif self.game_level.is_enemy_tank_at_position(tank.position.left()):
            tank.turn_left()

    def move_down(self, tank):
        if self.game_level.game_map.is_empty_space(pos=tank.position.down())\
                and not self.game_level.is_enemy_tank_at_position(tank.position.down()):
            tank.position = tank.position.down()
            tank.turn_down()
        elif self.game_level.is_enemy_tank_at_position(tank.position.down()):
            tank.turn_down()

    def move_right(self, tank):
        if self.game_level.game_map.is_empty_space(pos=tank.position.right())\
                and not self.game_level.is_enemy_tank_at_position(tank.position.right()):
            tank.position = tank.position.right()
            tank.turn_right()
        elif self.game_level.is_enemy_tank_at_position(tank.position.right()):
            tank.turn_right()

    def move_up(self, tank):
        if self.game_level.game_map.is_empty_space(pos=tank.position.up())\
                and not self.game_level.is_enemy_tank_at_position(tank.position.up()):
            tank.position = tank.position.up()
            tank.turn_up()
        elif self.game_level.is_enemy_tank_at_position(tank.position.up()):
            tank.turn_up()

    def shoot_projectile(self, tank):
        if tank.direction == 'l':
            start_pos = Position(tank.position.x - 1, tank.position.y)
            self.game_level.projectiles.append(Projectile(start_pos, 'l'))
        elif tank.direction == 'r':
            start_pos = Position(tank.position.x + 1, tank.position.y)
            self.game_level.projectiles.append(Projectile(start_pos, 'r'))
        elif tank.direction == 'd':
            start_pos = Position(tank.position.x, tank.position.y + 1)
            self.game_level.projectiles.append(Projectile(start_pos, 'd'))
        elif tank.direction == 'u':
            start_pos = Position(tank.position.x, tank.position.y - 1)
            self.game_level.projectiles.append(Projectile(start_pos, 'u'))

    def check_kill_count(self):
        if self.game_level.player_tank.kill_count == 5:
            self.set_game_over()

    def move_enemy_tanks(self):
        choices = {0: self.move_left,
                   1: self.move_up,
                   2: self.move_right,
                   3: self.move_down}
        for tank in self.game_level.enemy_tanks:
            if random.randint(0, 100) < 60:
                choices[random.randint(0, 3)](tank)

    def set_game_over(self):
        self.game_over = True

    def is_game_over(self):
        return self.game_over
