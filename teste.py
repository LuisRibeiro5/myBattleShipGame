# navio = {"posicao":[(1,2),(1,3),(1,4)]}
# x,y = navio["posicao"][0]
# print((x,y) in navio["posicao"])

# print(all(navio["posicao"]))
# i = 0
# while True:
#     navio["posicao"][i] = input("k: ").upper()
    
#     print(all(navio["posicao"]))
#     if all(ship == "X" for ship in navio["posicao"]):
#         print("navio destruido")
#         break
#     i += 1

def set_positions(initial_pos, size, orientation):
    positions = {}
    x,y = initial_pos

    for i in range(size):
        if orientation == "vertical":
            positions[ (x + i,y) ] = True
        else:#Horizontal
            positions[ (x,y + i) ] = True

    return positions

def seila():
    # positions = set_positions((0,0), 5, "vertical")
    # print(positions)
    # for pos in positions:
    #     print(pos, type(pos))
    # print(all([ positions.values()]))
    # print(None)
    # print(not None)
    x = 0
    y = 0
    for row in range(x - 1, x + 5 + 1):
            for j in range(-1,2):                
                print(f"[{row}][{y - j}]" )
                
def teste_ships():
    ships = {
        "Porta-avioes": (5,1),
        "Navios-tanque": (4,2),
        "Contratorpedeiros": (3,3),
        "Submarino": (2,4)
    }
    for ship_types in ships:
        name = ship_types
        size = ships[ship_types][0]
        num_ships = ships[ship_types][1]
        for ship in range(num_ships):
            print(f'{name} - {size} - {ship_types}\n')
            
def test_get_enemy_attack():
    import random
    x = random.randint(ord('A'),ord('J'))
    y = random.randint(0,9)
    print(x - ord("A"), y)
    
def test_ship_coordinates():
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
    ship = Ship("hulk", (0,0), 5, "vertical")
    for cords in ship.coordinates.keys():
        print(cords)
    
    for item in ship.coordinates.values():
        print(item)
        
    if all([value == False for value in ship.coordinates.values()]):
        print("Navio destruido")
    else:
        print("continua")
        
def teste_if_return_msg():
    def is_valid(palavra):
        if palavra == "boi":
            return "msg erro"
        if palavra == "animal":
            return "msg outroErro"

    erro = is_valid("animal")
    if erro:
        print(erro)
    else: 
        print("deu certo")
      
def teste_if():
    from src.ships.ships import Ship, is_valid_position
    from src.table.table import Table
    
    way = '1'
    player = Table()
    player.board[0][0] = "1"
    name = "Gigante"
    size = 5
    orientation = "vertical"
    x,y = (0,0)
    
    is_valid, msg = is_valid_position((x,y), size, orientation, player.board)
    
    if way == '1':
        print(msg)
    
    if is_valid:
        ship_instance = Ship(name, (x,y), size, orientation)
        player.place_ship(ship_instance)  
    
    print(is_valid)
    print(msg)
    
if __name__ == "__main__":
    # teste_if()
    teste_if()
               