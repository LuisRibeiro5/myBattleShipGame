from src.model.board import Board
from src.model.fleet import Fleet
from src.views.display_manager import DisplayManager
from src.views.input_handler import InputHandler

class TurnHandler:
    def __init__(self):
        self.player_board = Board()
        self.enemy_board = Board()
        self.player_fleet = Fleet()
        self.enemy_fleet = Fleet()
        self.display_manager = DisplayManager()
        self.input_handler = InputHandler()
    
    def setup_game(self, positioning_choice):
        if positioning_choice == "manual":
            self.player_fleet.setup_manual(self.player_board, self.display_manager, self.input_handler)
        else:
            self.player_fleet.setup_random(self.player_board)
        
        self.enemy_fleet.setup_random(self.enemy_board)
    
    def process_turn(self):
        
        self.player_turn()
        if self.check_winner():
            return
        
        self.enemy_turn()
        if self.check_winner():
            return
    
    def check_winner(self):
        if self.player_fleet.is_defeated():
            self.display_manager.show_winner("Enemy")
            return True
        elif self.enemy_fleet.is_defeated():
            self.display_manager.show_winner("Player")
            return True
        return False
    
    def get_winner(self):
        if self.player_fleet.is_defeated():
            return "Enemy"
        return "Player"

    def player_turn(self):
        self.display_manager.show_turn("Player")
        self.display_manager.show_boards(self.player_board, self.enemy_board)
        attack_coordinates = self.input_handler.get_player_attack()
        
        x,y = attack_coordinates
        if self.enemy_board.grid[x][y] in ['~','X']:
            print('Posição já foi atacada. Escolha outra.')
            self.player_turn() 
            return
        
        if self.enemy_board.is_hit(attack_coordinates):
            msg = self.enemy_fleet.ship_sunked(attack_coordinates)
            
            self.display_manager.show_hit("Player", msg)
            if self.enemy_fleet.is_defeated():
                return
            self.player_turn()
        else:
            self.display_manager.show_miss("Player")
    
    def enemy_turn(self):
        self.display_manager.show_turn("Enemy")
        enemy_attack = self.input_handler.get_enemy_attack()
        
        x,y = enemy_attack
        if self.player_board.grid[x][y] in ['~','X']:
            self.enemy_turn()
        
        if self.player_board.is_hit(enemy_attack):
            msg = self.player_fleet.ship_sunked(enemy_attack)
            
            self.display_manager.show_hit("Enemy", msg)
            if self.player_fleet.is_defeated():
                return
            self.enemy_turn()
        else:
            self.display_manager.show_miss("Enemy")