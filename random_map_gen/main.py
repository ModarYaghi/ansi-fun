from map import Map


def run() -> None:
    exit = False
    map_width, map_height = 50, 25
    while not exit:
        game_map = Map(map_width, map_height)
        game_map.display_map()
        if input("> ") == "q":
            exit = True


if __name__ == "__main__":
    run()