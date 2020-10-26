class Tank:
    def __init__(self, pos):
        self.direction = 'd'
        self.position = pos

    def turn_left(self):
        self.direction = 'l'

    def turn_down(self):
        self.direction = 'd'

    def turn_up(self):
        self.direction = 'u'

    def turn_right(self):
        self.direction = 'r'


class PlayerTank(Tank):
    def __init__(self, pos):
        super().__init__(pos)
        self.health = 5


class EnemyTank(Tank):
    def __init__(self, pos):
        super().__init__(pos)