from src.ships.ships import Ship

class Table:
    def __init__(self):
        self.board = [[" " for j in range(10)] for i in range(10)]
        self.game_board = [[" " for j in range(10)] for i in range(10)]
        self.ships = []
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
            print(x,y)
            self.board[x][y] = "1"
            
        pass
    
    def is_hit(self, coordinates):
        """
        Verifica oque foi atingido após o ataque inimigo.
        Se a coordenada no tabuleiro "self.board" for " " significa que errou o tiro e coloca "~", se acertou coloca "X".
        O tabuleiro alterado é sempre o do game board. 
        
        param: coordinates: tuple com x e y
        return: bool: True se acertou um navio
        """
        x,y = coordinates

        if self.board[x][y] == " ": 
            self.game_board[x][y] = "~"
            self.board[x][y] = "~"
            print("acertou o mar")
            return False
        
        #acertou um navio
        self.game_board[x][y] = "X"
        self.board[x][y] = "X"
        print("acertou um navio")
        self.ship_destroyed((x,y))
        return True
            
            
        
        # Verifica se um navio foi afundado
        #   Se foi colocar na lista sunks
    
    def ship_destroyed(self, coordinate):
        for ship in self.ships:
            for cords in ship.coordinates.keys():
                if cords == coordinate:
                    ship.coordinates[cords] = False
                    
                    #se essa condicao retornar True o navio foi destruido
                    if all([value == False for value in ship.coordinates.values()]):
                        print(f"Voce afundou o navio {ship.name}!!!")
                        self.sunks.append(ship)

                    return
                
        
    def reset_board(self):
        """
        Funcao criada para resetar os navios da table com intuito de realizar a escolha de navios aleatorios varias vezes.
        """
        self.board = [[" " for j in range(10)] for i in range(10)]
        
