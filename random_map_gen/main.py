from map import Map


def run() -> None:
    while True:
        game_map.display_map()
        input("> ")


if __name__ == "__main__":
    map_width, map_height = 30, 15
    game_map = Map(map_width, map_height)
    run()

