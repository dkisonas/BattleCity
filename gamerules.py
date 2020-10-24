import msvcrt


class GameRules:
    def __init__(self, game_level):
        self.game_level = game_level
        self.game_over = False

    def process_user_input(self):
        controls = {b'a': self.move_left,
                    b's': self.move_down,
                    b'd': self.move_right,
                    b'w': self.move_up,
                    b'q': self.set_game_over,
                    b'k': self.shoot_projectile}
        controls[msvcrt.getch()]()

    def move_left(self):
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.left())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.positions = pos_list

    def move_down(self):
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.down())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.positions = pos_list

    def move_right(self):
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.right())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.positions = pos_list

    def move_up(self):
        pos_list = []
        for pos in self.game_level.tank.positions:
            pos_list.append(pos.up())
        if self.game_level.game_map.is_empty_space(pos_list=pos_list):
            self.game_level.tank.positions = pos_list

    def shoot_projectile(self):
        return

    def set_game_over(self):
        self.game_over = True

    def is_game_over(self):
        return self.game_over
