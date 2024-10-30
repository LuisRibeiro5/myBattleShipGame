from src.model.ships import Ship
from src.config.game_config import ships_config, board_size
import random

class Fleet:
    def __init__(self):
        self.ships = []
    
    def setup_manual(self, board, display_manager, input_handler):
        for ship_name, (size, quantity) in ships_config.items():
            for _ in range(quantity):
                while True:
                    display_manager.display_positioning_screen(board, input_handler, ship_name, size)
                    x, y, orientation = display_manager.get_positioning_input(ship_name, size, input_handler)
                    ship = Ship(ship_name, size, (x, y), orientation)
                    if not ship.coordinates:
                        display_manager.show_invalid_position()
                        continue
                    if board.place_ship(ship):
                        self.ships.append(ship)
                        break
                    else:
                        display_manager.show_invalid_position()
    
    def setup_random(self, board):
        for ship_name, (size, quantity) in ships_config.items():
            for _ in range(quantity):
                while True:
                    x = random.randint(0, board_size - 1)
                    y = random.randint(0, board_size - 1)
                    orientation = random.choice(["horizontal", "vertical"])
                    ship = Ship(ship_name, size, (x, y), orientation)
                    if not ship.coordinates:
                        continue
                    if board.place_ship(ship):
                        self.ships.append(ship)
                        break
    
    def ship_sunked(self, attack_coordinates):
        msg = ""
        for i,ship in enumerate(self.ships):
            for j,cords in enumerate(ship.coordinates):
                if cords == attack_coordinates:
                    del ship.coordinates[j]
                    
                    if len(ship.coordinates) == 0:
                        self.ships[i].sunk = True
                        msg = f'afundou o {ship.name}' 
                        
                    return msg
    
    def is_defeated(self):
        return all(ship.sunk for ship in self.ships)