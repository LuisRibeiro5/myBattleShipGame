class View():
    def __init__(self) -> None:
        pass

    def show(self):
        pass

def aux_board(board):
    """
    Funcao auxiliar de print_boards, sua funcao é estregar uma lista de strings com as colunas de cada linha do tabuleiro.
    
    param: board: um tabuleiro, self.board de uma instancia de Table
    return: list: uma lista de strings a ser imprimidas posteriormente
    """
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

def print_boards(board1, enemy_board2):
    """
    Funcao que realiza print de dois tabuleiros um ao lado do outro
    
    param: board1: Table.board de um jogador
    param: enemy_board2: Outro Table.board porem do inimigo
    return: None 
    """
    for linha1, linha2 in zip(aux_board(board1), aux_board(enemy_board2)):
        print(linha1,"\t\t",linha2) 
        
def show_ships_on_board(board):
    """
    Recebe um tabuleiro para realizar o output
    
    :param board Table.board para fazer o print
    :return None
    """
    print(' '*4,"0   1   2   3   4   5   6   7   8   9  ")
    linha = 'A'
    for i,row in enumerate(board):
        print(chr(ord(linha) + i),end=" ")
        for col in row:
            print(f" | {col}",end="")
        print(' |\n','   ','-'*len(row)*4 + "-", sep='')
        
