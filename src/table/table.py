from src.ships.ships import Ship

class Table:
    def __init__(self):
        self.board = [[" " for j in range(10)] for i in range(10)]
        self.game_board = [[" " for j in range(10)] for i in range(10)]
        self.ships: Ship = []
        self.sunks = []
    
    def place_ship(self, ship: Ship):
        """
        Metodo que coloca a posicao de uma nova instancia de navio no tabuleiro, e adiciona a instancia do navio em uma lista com todos os navios.
        O tabuleiro que "recebe" as posicoes do navio é o board.
        
        :param ship: uma instancia de Ship
        :return None
        """
        self.ships.append(ship)
        for x,y in ship.coordinates:
            self.board[x][y] = "1"
            
        pass
    
    def is_hit(self, coordinates):
        # Verificar se uma coordenada foi atingida
        x,y = coordinates
        #se a coordenada no tabuleiro "escondido" for " " significa que errou o tiro, o tabuleiro alterado é sempre o do game board. 
        if self.board[x][y] == " ": 
            self.game_board[x][y] = "~"
            print("acertou o mar")
        
        elif self.board[x][y] == "1":#acertou um navio
            self.game_board[x][y] = "X"
            print("acertou um navio")
            self.ship_destroyed((x,y))
            
            
        
        # Verifica se um navio foi afundado
        #   Se foi colocar na lista sunks
    
    def ship_destroyed(self, coordinate):
        for ship in self.ships:
            for cords in ship.keys():
                if cords == coordinate:
                    ship[cords] = False
                    
                    #se essa condicao retornar True significa que todos
                    #navios foram destruidos
                    if not all([ship.values()]):
                        print("Voce afundou um navio!!!")
                        self.sunks.append(ship)

                    return
                
        
    def display(self):
        # Exibir o tabuleiro para o jogador
        pass
