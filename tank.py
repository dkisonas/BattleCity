from position import Position


class Tank:
    def __init__(self, pos):
        self.direction = 'd'
        self.core = Position(pos.x, pos.y)
        self.positions = [
            Position(pos.x - 1, pos.y),
            Position(pos.x + 1, pos.y),
            Position(pos.x, pos.y + 1)
        ]

    def turn_left(self):
        self.direction = 'l'
        self.positions = [
            Position(self.core.x, self.core.y - 1),
            Position(self.core.x, self.core.y + 1),
            Position(self.core.x - 1, self.core.y)
        ]

    def turn_down(self):
        self.direction = 'd'
        self.positions = [
            Position(self.core.x - 1, self.core.y),
            Position(self.core.x + 1, self.core.y),
            Position(self.core.x, self.core.y + 1)
        ]

    def turn_up(self):
        self.direction = 'u'
        self.positions = [
            Position(self.core.x - 1, self.core.y),
            Position(self.core.x + 1, self.core.y),
            Position(self.core.x, self.core.y - 1)
        ]

    def turn_right(self):
        self.direction = 'r'
        self.positions = [
            Position(self.core.x, self.core.y - 1),
            Position(self.core.x, self.core.y + 1),
            Position(self.core.x + 1, self.core.y)
        ]
