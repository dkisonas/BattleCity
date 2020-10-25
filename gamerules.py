import msvcrt

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
        controls[input()]()

    def move_left(self):
        if self.game_level.game_map.is_empty_space(pos=self.game_level.player_tank.position.left()):
            self.game_level.player_tank.position = self.game_level.player_tank.position.left()
            self.game_level.player_tank.turn_left()

    def move_down(self):
        if self.game_level.game_map.is_empty_space(pos=self.game_level.player_tank.position.down()):
            self.game_level.player_tank.position = self.game_level.player_tank.position.down()
            self.game_level.player_tank.turn_down()

    def move_right(self):
        if self.game_level.game_map.is_empty_space(pos=self.game_level.player_tank.position.right()):
            self.game_level.player_tank.position = self.game_level.player_tank.position.right()
            self.game_level.player_tank.turn_right()

    def move_up(self):
        if self.game_level.game_map.is_empty_space(pos=self.game_level.player_tank.position.up()):
            self.game_level.player_tank.position = self.game_level.player_tank.position.up()
            self.game_level.player_tank.turn_up()

    def shoot_projectile(self):
        if self.game_level.player_tank.direction == 'l':
            start_pos = Position(self.game_level.player_tank.position.x - 1, self.game_level.player_tank.position.y)
            self.game_level.projectiles.append(Projectile(start_pos, 'l'))
        if self.game_level.player_tank.direction == 'r':
            start_pos = Position(self.game_level.player_tank.position.x + 1, self.game_level.player_tank.position.y)
            self.game_level.projectiles.append(Projectile(start_pos, 'r'))
        if self.game_level.player_tank.direction == 'd':
            start_pos = Position(self.game_level.player_tank.position.x, self.game_level.player_tank.position.y + 1)
            self.game_level.projectiles.append(Projectile(start_pos, 'd'))
        if self.game_level.player_tank.direction == 'u':
            start_pos = Position(self.game_level.player_tank.position.x, self.game_level.player_tank.position.y - 1)
            self.game_level.projectiles.append(Projectile(start_pos, 'u'))

    def set_game_over(self):
        self.game_over = True

    def is_game_over(self):
        return self.game_over
