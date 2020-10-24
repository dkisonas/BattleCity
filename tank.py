from position import Position


class Tank:
    def __init__(self, pos):
        self.tank = [
            [1, 1, 1],
            [0, 1, 0]
        ]
        self.positions = [
            Position(pos.x - 1, pos.y),
            Position(pos.x, pos.y),
            Position(pos.x + 1, pos.y),
            Position(pos.x, pos.y + 1)
        ]
