from random import randint
from tile import Tile, plains, forest, pines, mountain, water


class Map:
    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        self.width = width
        self.height = height

        self.map = list[list[Tile]]

        self.generate_map()

        self.generate_patch(forest, 3, 3, 5)
        self.generate_patch(pines, 3, 3, 5)
        self.generate_patch(mountain, 3, 3, 5)

    def generate_map(self) -> None:
        self.map_data = [[plains for _ in range(self.width)] for _ in range(self.height)]

    def generate_patch(self, tile: Tile, num_patches: int, min_size: int, max_size: int, irregular: bool = True) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile


    def display_map(self) -> None:
        frame = "x" + self.width * "=" + "x"
        print(frame)
        for row in self.map_data:
            row_tiles = [tile.symbol for tile in row]
            print("|" + "".join(row_tiles) + "|")
        print(frame)

