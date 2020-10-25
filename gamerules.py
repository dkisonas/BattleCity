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
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.left())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.core = self.game_level.tank.core.left()
            self.game_level.tank.positions = pos_list
            self.game_level.tank.turn_left()

    def move_down(self):
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.down())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.core = self.game_level.tank.core.down()
            self.game_level.tank.positions = pos_list
            self.game_level.tank.turn_down()

    def move_right(self):
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.right())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.core = self.game_level.tank.core.right()
            self.game_level.tank.positions = pos_list
            self.game_level.tank.turn_right()

    def move_up(self):
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.up())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.core = self.game_level.tank.core.up()
            self.game_level.tank.positions = pos_list
            self.game_level.tank.turn_up()

    def shoot_projectile(self):
        if self.game_level.tank.direction == 'l':
            start_pos = Position(self.game_level.tank.core.x - 2, self.game_level.tank.core.y)
            self.game_level.projectiles.append(Projectile(start_pos, 'l'))
        if self.game_level.tank.direction == 'r':
            start_pos = Position(self.game_level.tank.core.x + 2, self.game_level.tank.core.y)
            self.game_level.projectiles.append(Projectile(start_pos, 'r'))
        if self.game_level.tank.direction == 'd':
            start_pos = Position(self.game_level.tank.core.x, self.game_level.tank.core.y + 2)
            self.game_level.projectiles.append(Projectile(start_pos, 'd'))
        if self.game_level.tank.direction == 'u':
            start_pos = Position(self.game_level.tank.core.x, self.game_level.tank.core.y - 2)
            self.game_level.projectiles.append(Projectile(start_pos, 'u'))

    def set_game_over(self):
        self.game_over = True

    def is_game_over(self):
        return self.game_over
