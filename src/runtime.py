from table.table import Table
from src.ships.ships import *
from src.views.player_time import get_player_attack, display_player_turn
from src.views.enemy_time import get_enemy_attack, display_enemy_turn
from src.views.home import display_home_menu
from src.views.view import print_boards
import random

class Runtime:
    def __init__(self):
        self.player_table = Table()
        self.enemy_table = Table()
    
    def start_game(self):
        # Iniciar o jogo e o loop principal
        display_home_menu()
        
        self.initialize_ships(self.player_table)
        self.initialize_ships(self.enemy_table)
        
        key = 0
        while True:
            if key == 0:
                self.handle_player_turn()
                key = 1
            else:
                self.handle_enemy_turn()
                key = 0
            
            if self.check_winner():
                break
        
        print("fim!")
        display_home_menu()
    
    def handle_player_turn(self):
        display_player_turn()
        print_boards(self.player_table.board,self.enemy_table.game_board)
        
        while True:
            coordinate = get_player_attack()
            x,y = coordinate
            if self.enemy_table.game_board[x][y] == " ":
                break
            print("Essa posicao ja foi atacada")
            
        self.enemy_table.is_hit(coordinate)
        #adicionar no is hit uma verificacao para caso a posicao escolhida ja tenha sido atacada
        print_boards(self.player_table.board,self.enemy_table.game_board)
    
    def handle_enemy_turn(self):
        # Logica para turno do inimigo
        display_enemy_turn()
        
        while True:
            coordinate = get_enemy_attack()
            x,y = coordinate
            if self.player_table.game_board[x][y] == " ":
                break
            print("Essa posicao ja foi atacada")
        
        self.player_table.is_hit(coordinate)
        print_boards(self.player_table.board,self.enemy_table.game_board)
        
    
    def check_winner(self):
        # Verificar se há um vencedor
        pass
    
    def initialize_ships(self, player: Table):
        """
        função para inicializar e colocar os navios no tabuleiro de um player. 
        Usa funcoes de validacao para a escolha das posicoes do navio do player. Para o pc usa o modulo ramdom para fazer as escolhas.
        
        :param player: class Table representando board do jogador
        
        :return None: 
        """
        for ship in ships:
            name = ship
            size = ships[ship]
            while True:
                if player == self.player_table:
                    orientation = get_orientation()
                    x,y = get_valid_xy()
                else:
                    orientation = random.choice(["vertical","horizontal"])
                    x = random.randint(0,9)
                    y = random.randint(0,9)
            
                if is_valid_position((x,y), size, orientation, player):
                    ship_instance = Ship(name, (x,y), size, orientation)
                    player.place_ship(ship_instance)
                    break     
