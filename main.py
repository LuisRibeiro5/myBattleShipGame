MIN_ROW = "A"
MAX_ROW = "J"
MIN_COL = 0
MAX_COL = 9


tables = {
    "player": [[" " for i in range(10)] for j in range(10)],
    "print_player": [[" " for i in range(10)] for j in range(10)],
    "pc": [[" " for i in range(10)] for j in range(10)],
    "print_pc": [[" " for i in range(10)] for j in range(10)]
}

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

def ship_fits_in_board(initial_pos,ship_size,ship_orientation, board):
    x,y = initial_pos

    if ship_orientation == "horizontal":
        if y - 1 + ship_size > 9:#-1 porque incluimos a posicao inicial na contagem
            return False         #(1,5) + 5(ship_size) *navio comeca na posicao 5 e acaba na 9. Dentro do range.
        else:
            if x - 1 + ship_size > 9:
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

def build_ship(nome,initial_pos,size,orientation):
    ship = {
        "nome": nome,
        "orientation": orientation,
        "initial_pos": initial_pos,
        "size": size
    }

    positions = {}
    x,y = initial_pos

    for i in range(size):
        if orientation == "vertical":
            positions[ (x + i,y) ] = True
        else:#Horizontal
            positions[ (x,y + i) ] = True

    ship["positions"] = positions
    return ship

def init_ships_on_board(ships,board):
    for ship in ships:
        name = ship
        size = ships[ship]
        x,y = get_valid_xy()
        orientation = get_orientation()
        if ship_fits_in_board((x,y), size, orientation, board):
            build_ship(name,(x,y), size, orientation)
            #colocar navios no tabuleiro
            

def aux_board(board):
    board_str = ""
    letra = "A"
    board_str += ' '*4 + "0   1   2   3   4   5   6   7   8   9  \n"
    for i in range(10):
        board_str += f"{chr(ord(letra) + i)}"
        for j in range(10):
            board_str += f" | {board[i][j]}"
        board_str += " | \n"
    board_return = board_str.split("\n")
    return board_return

def print_board(board1, board2):
    for linha1, linha2 in zip(aux_board(board1), aux_board(board2)):
        print(linha1,"\t\t",linha2) 

if __name__ == "__main__":
    # ship = build_ship("ola", ("A",1), 5, "vertical")
    # print(ship)
    # show_boards(tables["player"], tables["pc"])
    # print_boards(tables["player"])
    # print_board(tables["pc"],tables["player"])
    while True:
        x = input("te: ")
        print(f"{ord(x) - ord('A')}")