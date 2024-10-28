from src.table.table import Table
from src.ships.ships import *
from src.views.player_time import get_player_attack, display_player_turn
from src.views.enemy_time import get_enemy_attack, display_enemy_turn
from src.views.home import display_home_menu
from src.views.view import print_boards,print_self_board, print_ship_animation
import os
import time
import random
random.seed(1)

class Runtime:
    def __init__(self):
        self.player_table = Table()
        self.enemy_table = Table()
    
    def start_game(self):
        # Iniciar o jogo e o loop principal
        self.start_menu()
        self.start_ships()
        
        while True:
            self.handle_player_turn()
            if self.check_winner():
                break
            
            self.handle_enemy_turn()
            if self.check_winner():
                break
            
        print("fim!")
        display_home_menu()
    
    def start_menu(self):
        print_ship_animation()
        self.next()
        display_home_menu()
        self.next()
               
    def handle_player_turn(self):
        while True:
            display_player_turn()
            print_boards(self.player_table.board,self.enemy_table.game_board)
            
            coordinate = get_player_attack()
            self.next()
            x,y = coordinate
            if self.enemy_table.game_board[x][y] == " ":
                break
            print("Essa posicao ja foi atacada")
            
        if self.enemy_table.is_hit(coordinate):
            print("**** Voce pode atirar de novo! ****")
            self.next(2.5)
            self.handle_player_turn()
        #adicionar no is hit uma verificacao para caso a posicao escolhida ja tenha sido atacada
        print_boards(self.player_table.board,self.enemy_table.game_board)
        self.next(2.5)
    
    def handle_enemy_turn(self):
        # Logica para turno do inimigo
        display_enemy_turn()
        print_boards(self.player_table.board,self.enemy_table.game_board)
        
        while True:
           
            coordinate = get_enemy_attack()
            x,y = coordinate
            if self.player_table.game_board[x][y] == " ":
                break
            #print("Essa posicao ja foi atacada")
            
        self.next(2)
        if self.player_table.is_hit(coordinate):
            print("**** Ele pode atirar de novo! ****")
            self.next(2.5)
            self.handle_enemy_turn()
        print_boards(self.player_table.board,self.enemy_table.game_board)
        self.next(2.5)
        
    
    def check_winner(self):
        # Verificar se há um vencedor
        if len(self.player_table.sunks) == 10:
            print("Todos os navios foram afundado, O PC venceu!!")
            return True
        elif len(self.enemy_table.sunks) == 10:
            print("Todos os navios foram afundado, O PLAYER venceu!!")
            return True
    
    def start_ships(self):
        while True:
            print("="*27)
            print("escolhendo navios do player")
            print("="*27)
            
            print("1 - escolher navios")
            print("2 - navios aleatorios")
            resp = input(">")
            self.next()
            
            if resp not in ["1","2"]: continue 
            
            while True:
                self.initialize_ships(self.player_table, resp)
                
                while True:    
                    self.next()
                    print_self_board(self.player_table.board)
                    
                    print("0 - confirm")
                    print("1 - escolher navios")
                    print("2 - navios aleatorios")
                    resp = input(">")
                    self.next()
                    if resp not in ["0","1","2"]:
                        continue
                    break
                
                if resp == "0":
                    print("Seus navios foram posionados!!")
                    self.next(1)
                    break
                
                self.player_table.reset_board()
                    
            break
        
        print("====escolhendo navios do pc====\n")
        time.sleep(2)
        self.initialize_ships(self.enemy_table)
        print("==== Navios do PC posicionados!!! ====")
        self.next(1.3)
    
    def initialize_ships(self, player: Table, way = ""):
        """
        função para inicializar e colocar os navios no tabuleiro de um player. 
        Usa funcoes de validacao para a escolha das posicoes do navio do player. Para o pc usa o modulo ramdom para fazer as escolhas.
        
        :param player: class Table representando board do jogador
        
        :return None: 
        """
        # import pdb; pdb.set_trace()
        msg = " "
        for ship_types in ships:
            
            name = ship_types
            size = ships[ship_types][0]
            num_ships = ships[ship_types][1]
            
            for ship in range(num_ships):
                while True:
                    if  way == "1":
                        self.next(wait=0.2)
                        print(msg)
                        print_self_board(player.board)
                        
                        x,y = get_valid_xy()
                        orientation = get_orientation()
                    else:
                        orientation = random.choice(["vertical","horizontal"])
                        x = random.randint(0,9)
                        y = random.randint(0,9)
                        
                    is_valid, msg = is_valid_position((x,y), size, orientation, player.board)
                        
                    #Se é valido coloca o navio
                    if is_valid:
                        ship_instance = Ship(name, (x,y), size, orientation)
                        player.place_ship(ship_instance)
                        break  
            
    def next(self, wait=0.2):
        time.sleep(wait)
        os.system('cls' if os.name == 'nt' else 'clear')
        
    
    def test_print_boards(self):
        # print_boards(self.player_table.board, self.enemy_table.board)
        print_ship_animation()
        display_home_menu()


#printar um erro apenas de way for == '1'
#   se way == 1 printa