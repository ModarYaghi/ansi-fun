from colorama import init, Fore


init()


ANSI_RESET = Fore.RESET
ANSI_YELLOW = Fore.YELLOW
ANSI_GREEN = Fore.GREEN
ANSI_BLUE = Fore.BLUE
ANSI_RED = Fore.RED
ANSI_WHITE = Fore.WHITE
ANSI_MAGENTA = Fore.MAGENTA
ANSI_CYAN = Fore.CYAN


class Tile:
    def __init__(
        self, symbol: str, color: str = ANSI_RESET, colored: bool = True
    ) -> None:
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if colored else symbol


plains = Tile(".", ANSI_YELLOW)
forest = Tile("8", ANSI_GREEN)
pines = Tile("Y", ANSI_GREEN)
mountain = Tile("A", ANSI_WHITE)
water = Tile("~", ANSI_CYAN)
