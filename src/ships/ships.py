ships = {
    #Tupla[0] tamanho do navio
    #Tupla[1] quantidades de navio daquele tipo
    
        "Porta-avioes": (5,1), 
        "Navios-tanque": (4,2),
        "Contratorpedeiros": (3,3),
        "Submarino": (2,4)
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
                self.coordinates[ (x + i,y) ] = True
            else:#Horizontal
                self.coordinates[ (x,y + i) ] = True

def get_valid_xy():
    while True:
        try:
            x = input("position x: ").upper()
            x = ord(x) - ord("A")#converte para idx da row
            if x < 0 or x >= 10:
                print("choose a x between A - J")
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
        print("nao coube na tabela")
        return False
    
    if ship_orientation == "vertical":
        #for aninha que verifica se posição e posições em volta estão livres ou não
        for row in range(x - 1, x + ship_size + 1):
            for j in range(-1,2):
                try:
                    if board[row][y - j] != " ":
                        print("Tem navio perto!")
                        return False
                except:
                    continue
        
    else:#horizontal
        for i in range(-1,2):
            for col in range(y - 1, y + ship_size + 1):
                try:
                    if board[x - i][col] != " ":
                        print(f'{x - i} {col}')
                        print("Tem navio perto!")
                        return False
                except:
                    continue
                
    print("pos valida")
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
    return True
        