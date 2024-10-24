from .table.table import Table
import random
from os import system
import time

class Runtime():
    def __init__(self) -> None:
        self.step = "start" 
        self.state = "stopped"
        self.history = []
        
    def start(self):
        print('Bem vindo a batalha naval')
        self.state = "running"
        self.history.append("Runtime started")
        self.run()        
    
    def execute_step(self, next_step):
        print('O jogo está iniciando...')
        self.history.append(f"{self.step} to {next_step}")
        self.step = next_step
    
    def run(self):
        while self.state == "running":
            
            if self.step == "start":
                self.execute_step("initializing")
                player = Table()
                player.show_pretty_table()
                player.set_all_ships_position()
                
                pc = Table()
                pc.set_pc_all_ships_positon()
                print("Navios de ambos posicionados.")
                
            elif self.step == "initializing":
                self.execute_step("processing")
                current_player = random.choice([player,pc])
                while True:
                    system("clear")
                    print(f'vez do {"pc" if current_player == pc else "player"}')
                    
                    if current_player == pc:
                        current_player.pc_attack(player)
                        print("PC ATACK ON YOUR BOARD:")
                        player.show_game_table()
                        time.sleep(2)
                    else:
                        print("PC BOARD: ")
                        pc.show_game_table()
                        current_player.pc_attack(pc)
                        print("YOU ATTACKED: ")
                        pc.show_game_table()
                        time.sleep(2)
                    
                    
                    if player.ships_left() == 0:
                        print("fim de jogo, pc ganhou")
                        self.state = "finish"
                        break
                    if pc.ships_left() == 0:
                        print("fim de jogo, pc ganhou")
                        self.state = "finish"
                        break
                    
                    current_player = player if current_player == pc else pc
