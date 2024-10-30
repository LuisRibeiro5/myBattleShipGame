from src.controllers.turn_handler import TurnHandler
from src.views.display_manager import DisplayManager

class GameLoop:
    def __init__(self):
        self.turn_handler = TurnHandler()
        self.display_manager = DisplayManager()
    
    def start_game(self):
        self.display_manager.show_welcome()
        
        if self.display_manager.display_home_menu() == "start":
            positioning_choice = self.display_manager.display_positioning_menu()
            self.turn_handler.setup_game(positioning_choice)
        
        while not self.turn_handler.check_winner():
            self.turn_handler.process_turn()
        
        self.display_manager.show_winner(self.turn_handler.get_winner())
