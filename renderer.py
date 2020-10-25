from position import Position
from time import sleep


def render_map(game_level):
    for i, row in enumerate(game_level.game_map.game_map):
        for j, column in enumerate(row):
            find = False
            for tank in game_level.enemy_tanks:
                if tank.position.at(j, i):
                    print("8", end="", flush=True)
                    find = True
                    break
            if find:
                continue
            if game_level.player_tank.position.at(j, i):
                print("*", end="", flush=True)
            elif game_level.game_map.is_projectile(x=j, y=i):
                print("@", end="", flush=True)
            elif game_level.game_map.is_empty_space(x=j, y=i):
                print(" ", end="", flush=True)
            elif game_level.game_map.is_wall(x=j, y=i) or game_level.game_map.is_border(x=j, y=i):
                print("#", end="", flush=True)
        print()


def render_projectiles(game_level):
    for p in game_level.projectiles:
        while not game_level.game_map.is_wall(x=p.position.x, y=p.position.y):
            if game_level.game_map.is_border(x=p.position.x, y=p.position.y):
                break
            if game_level.delete_enemy_tank_if_at_position(p.position):
                break
            temp = game_level.game_map.game_map[p.position.y][p.position.x]
            game_level.game_map.game_map[p.position.y][p.position.x] = 2
            render_map(game_level)
            game_level.game_map.game_map[p.position.y][p.position.x] = temp
            if p.direction == 'l':
                p.position.x -= 1
            elif p.direction == 'r':
                p.position.x += 1
            elif p.direction == 'u':
                p.position.y -= 1
            elif p.direction == 'd':
                p.position.y += 1
            sleep(0.05)
        if game_level.game_map.is_wall(x=p.position.x, y=p.position.y):
            game_level.game_map.game_map[p.position.y][p.position.x] = 0
        game_level.projectiles.remove(p)
