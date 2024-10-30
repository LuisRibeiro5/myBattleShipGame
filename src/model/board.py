from src.config.game_config import board_size

class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(board_size)] for _ in range(board_size)]
    
    def place_ship(self, ship):
        for (x, y) in ship.coordinates:
            if not (0 <= x < board_size and 0 <= y < board_size):
                return False
            if self.grid[x][y] != " ":
                return False
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < board_size and 0 <= ny < board_size:
                        if self.grid[nx][ny] == "S":
                            return False
        for (x, y) in ship.coordinates:
            self.grid[x][y] = "S"
        return True
    
    def is_hit(self, coordinates):
        x, y = coordinates
        if self.grid[x][y] == "S":
            self.grid[x][y] = "X"
            return True
        elif self.grid[x][y] == " ":
            self.grid[x][y] = "~"
            return False
        else:
            return False
    
    def display(self):
        header = "  " + "   ".join(map(str, range(board_size)))
        print(header)
        for i, row in enumerate(self.grid):
            row_str = chr(i + 65) + " " + " | ".join(row)
            print(row_str)