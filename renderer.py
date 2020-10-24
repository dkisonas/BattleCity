def render_map(game_level):
    for i, row in enumerate(game_level.game_map.game_map):
        for j, column in enumerate(row):
            if game_level.tank.position.at(j, i):
                print("T", end="", flush=True)
            elif game_level.game_map.is_empty_space(x=j, y=i):
                print(" ", end="", flush=True)
            elif game_level.game_map.is_wall(x=j, y=i):
                print("#", end="", flush=True)
        print()
