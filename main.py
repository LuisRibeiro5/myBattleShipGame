tables = {
    "player": [[" " for i in range(10)] for j in range(10)],
    "print_player": [[" " for i in range(10)] for j in range(10)],
    "pc": [[" " for i in range(10)] for j in range(10)],
    "print_pc": [[" " for i in range(10)] for j in range(10)]
}

def get_valid_xy():
    while True:
        try:
            x = int(input("position x: "))
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

def ship_fits_in_board(ship: dict, board):
    x,y = ship["initial_pos"]
    orientation = ship["orientation"]
    size = ship["size"]

    if orientation == "horizontal":
        if y - 1 + size > 9:#-1 porque incluimos a posicao inicial na contagem
            return False         #(1,5) + 5(size) *navio comeca na posicao 5 e acaba na 9. Dentro do range.
        else:
            if x - 1 + size > 9:
                return False

    if orientation == "vertical":
        for j in range(-1,2):
            for i in range(-1,size + 1): 
                try:
                    if board[x + i][y + j] != " ":
                        return False
                except:
                    continue
    else:#horizontal
        for j in range(-1,2):
            for i in range(-1,size + 1): 
                try:
                    if board[x + j][y + i] != " ":
                        return False
                except:
                    continue


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
            positions[ (chr(ord(x) + i),y) ] = True
        else:#Horizontal
            positions[ [x][y + i] ] = True

    ship["positions"] = positions
    return ship

# def show_boards(board1, board2):
#     print(' '*4,"0   1   2   3   4   5   6   7   8   9  " + " "*12 + "   0   1   2   3   4   5   6   7   8   9  " )
#     letra = "A"
#     for i in range(10):
#         print(chr(ord(letra) + i),end=" ")
#         for j in range(10):
#             print(f" | {board1[i][j]}",end="")
#         print(" |\t\t", end="")
#         for j in range(10):
#             print(f"{chr(ord(letra) + i)} | {board2[i][j]}",end="")
#         print(' |\n','   ','-'*len(board1)*4 + " "*14 + "-"*len(board2)*4 + "-", sep='')


def aux_board(board):
    qua = ""
    letra = "A"
    qua += ' '*4 + "0   1   2   3   4   5   6   7   8   9  \n"
    for i in range(10):
        qua += f"{chr(ord(letra) + i)}"
        for j in range(10):
            qua += f" | {board[i][j]}"
        qua += " | \n"
    qua_return = qua.split("\n")

    return qua_return
    for item in qua_return:
        print(item)

def aux_board(board1, board2):
    for linha1, linha2 in zip(aux_board(board1), aux_board(board2)):
        print(linha1,"\t\t",linha2) 

if __name__ == "__main__":
    # ship = build_ship("ola", ("A",1), 5, "vertical")
    # print(ship)
    # show_boards(tables["player"], tables["pc"])
    # print_boards(tables["player"])
    aux_board(tables["pc"],tables["player"])