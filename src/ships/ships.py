ships = {
    "Porta-avioes": 5,
    "Navios-tanque": 4,
    "Navios-tanque": 4,
    "Contratorpedeiros": 3,
    "Contratorpedeiros": 3,
    "Contratorpedeiros": 3,
    "Submarino": 2,
    "Submarino": 2,
    "Submarino": 2,
    "Submarino": 2
}

class Ship:
    def __init__(self, name, initial_pos, size, orientation):
        self.name = name
        self.initial_pos = initial_pos
        self.orientation = orientation
        self.size = size
        self.coordinates = {}
        self.sunk = False
          
        #inicializa todas posições do navio no tabuleiro
        x,y = self.initial_pos

        for i in range(self.size):
            if self.orientation == "vertical":
                self.positions[ (x + i,y) ] = True
            else:#Horizontal
                self.positions[ (x,y + i) ] = True
    
    def is_sunk(self):
        # Verificar se o navio foi afundado
        
        pass

def get_valid_xy():
    while True:
        try:
            x = input("position x: ")
            x = ord(x) - ord("A")#converte para idx da row
            if x < 0 or x >= 10:
                print("choose a x between 0 - 9")
                continue
            y = int(input("position y: "))
            if y < 0 or y >= 10:
                print("choose a y between 0 - 9")
                continue
            break
        except:
            print("posicao invalida")
    return (x,y)

def get_orientation():
    while True:
            pos_input = input("horizontal(1) or vertical(2): ")
            if pos_input not in ['1','2']:
                print("invalid position(1 or 2)")
                continue
            elif pos_input == '1':
                return 'horizontal'
            else:
                return 'vertical' 

def is_valid_position(initial_pos,ship_size,ship_orientation, board):
    """
    Valida se existe navio na posicao escolhida ou em volta (navio nao pode estar colado em outro), é usado um for aninhado onde, dependendo da orientacao, ele itera na posicao em volta da que foi escolhida.
    
    param: initital_pos: tupla com coordenadas
    param: ship_size: int informando tamanho dos navios
    param: ship_orientation: string com "vertical" ou "horizontal"
    param: board: Table.board para validar as posicoes
    return: bool: retorna True se a posicao esta disponivel
    """
    x,y = initial_pos

    if not fits_in_table(initial_pos, ship_size, ship_orientation):
        return False
    
    if ship_orientation == "vertical":
        #for aninha que verifica se posição e posições em volta estão livres ou não
        for j in range(-1,2):
            for i in range(-1,ship_size + 1): 
                try:
                    if board[x + i][y + j] != " ":
                        return False
                except:
                    continue
    else:#horizontal
        for i in range(-1,2):
            for j in range(-1,ship_size + 1): 
                try:
                    if board[x + i][y + j] != " ":
                        return False
                except:
                    continue
    return True

def fits_in_table(initial_pos, ship_size,ship_orientation):
    """
    Essa funcao verifica se a posicao inicial escolhida + o tamanho do navio nao ultrapassa os limites do tabuleiro, evitando indexError.
    
    param: initial_pos: tupla com coordenadas iniciais escolhidas pelo player
    param: ship_size: int informando tamanho do navio
    param: ship_orientation: string com "vertical" ou "horizontal"
    return: bool: Se o navio cabe(É uma initial_pos válida) retorna True
    """
    x,y = initial_pos
    
    if ship_orientation == "horizontal":
        if y - 1 + ship_size > 9:#-1 porque incluimos a posicao inicial na contagem
            return False         #(1,5) + 5(ship_size) *navio comeca na posicao 5 e acaba na 9. Dentro do range.
        else:
            if x - 1 + ship_size > 9:
                return False