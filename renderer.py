from position import Position


def render_map(game_level):
    for i, row in enumerate(game_level.game_map.game_map):
        for j, column in enumerate(row):
            if Position(j, i) in game_level.tank.positions:
                print("*", end="", flush=True)
            elif game_level.game_map.is_empty_space(x=j, y=i):
                print(" ", end="", flush=True)
            elif game_level.game_map.is_wall(x=j, y=i):
                print("#", end="", flush=True)
        print()
