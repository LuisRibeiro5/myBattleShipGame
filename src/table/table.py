import random

class Table():
    def __init__(self) -> None:
        self.table = [] # tabuleiro tudo com 0 para vazio 1 para navio e x para lugar atingido
        self.game_table = []
        self.ships = {
            "Porta-avioes": [(), 5, ''], # posicao e o espaco que ocupa
            "Navios-tanque": [() ,4,''],
            "Contratorpedeiros": [(),2, ''],
            "Submarinos": [(), 1, '']
        } # dentro desse objeto vai ter todos os navios
        self.__build_tables()
    
    def __build_tables(self):
        for _ in range(10):
            linha = []
            for i in range(10):
                linha.append(0)
            self.table.append(linha)
        for _ in range(10):
            linha = []
            for i in range(10):
                linha.append(" ")
            self.game_table.append(linha)
    
    def player_attack(self, target):
        while True:
            print("escolha a coordenada que voce vai atacar: ")
            x,y = self.__get_valid_x_y()
            if target.game_table[x][y] != " ":
                print("position already attacked, choose other.")
                continue
            break
        if target.table[x][y] == 1:
            target.game_table[x][y] = "X"
            target.table[x][y] = 0
        else:
            target.game_table[x][y] = "~"
            
    def pc_attack(self, target):
        while True:
            print("escolha a coordenada que voce vai atacar: ")
            x = random.randint(0,9)
            y = random.randint(0,9)
            if target.game_table[x][y] != " ":
                print("position already attacked, choose other.")
                continue
            break
        if target.table[x][y] == 1:
            target.game_table[x][y] = "X"
            target.table[x][y] = 0
        else:
            target.game_table[x][y] = "~"
            
    def set_pc_all_ships_positon(self):
        for navio in self.ships:
            data_ship = self.ships[navio]
            data_ship[0],data_ship[2] = self.__set_pc_ship_position(data_ship)
            self.__put_ship_in_table(data_ship)
    
    def __set_pc_ship_position(self,ship):
        while True:
            x = random.randint(0,9)
            y = random.randint(0,9)
            position = random.choice(['horizontal','vertical']) 
            #verificar se navio cabe na posicao dependendo se é horizontal ou vertical
            if not self.__fits_in_table(x,y,position,ship[1]):
                print("it not fits in table, choose better position")
                continue
            #verificar se tem um navio na mesma posicao + 1 espaco
            if self.__there_is_already_a_ship(x,y,position,ship[1]) == None:
                print("theres already a ship in this local, choose a better position")
                continue
            break
        return (x,y),position
    
    def set_all_ships_position(self):
        for navio in self.ships:
            data_ship = self.ships[navio]
            print(f"{navio} - size:{data_ship[1]}")
            data_ship[0],data_ship[2] = self.__set_ship_position(data_ship)
            self.__put_ship_in_table(data_ship)
            self.show_pretty_table()
            
    def __put_ship_in_table(self,data_ship):
            # nome,data = data_ship.items()
            size = data_ship[1]
            x,y = data_ship[0]
            pos = data_ship[2]
            for i in range(size):
                if pos == "vertical":
                    self.table[x + i][y] = 1
                else:#Horizontal
                    self.table[x][y + i] = 1        
            
    def __set_ship_position(self,ship):
        while True:
            x,y = self.__get_valid_x_y()
            position = self.__get_valid_position() 
            #verificar se navio cabe na posicao dependendo se é horizontal ou vertical
            if not self.__fits_in_table(x,y,position,ship[1]):
                print("it not fits in table, choose better position")
                continue
            #verificar se tem um navio na mesma posicao + 1 espaco
            if self.__there_is_already_a_ship(x,y,position,ship[1]) == None:
                print("theres already a ship in this local, choose a better position")
                continue
            break
        return (x,y),position
        
    def __there_is_already_a_ship(self,x,y,position,ship_size):
        if position == "vertical":#verificacao onde navio esta na vertical, [x + n][y]
            for i in range(ship_size):
                if self.table[x + i][y] == 1:#se tem navio exatamente na posicao escolhida
                    print(f'there is already a ship in {x+i,y}')
                    return
                if y < 9:#para evitar outofrange
                    if self.table[x + i][y + 1] == 1:#se tem navio na coluna do lado direito
                        print(f"there is a ship on the right column {x + i,y + 1}")
                        return
                if y > 0:#para evitar outofrange
                    if self.table[x + i][y - 1] == 1:#se tem navio na coluna do lado esquerdo
                        print(f"there is a ship on the left column {x + i,y - 1}")
                        return
            if x + ship_size < 10:#para evitar outofrange
                if self.table[x + ship_size][y] == 1:#se tem navio na frente, linha da frente
                    print(f"there is a ship in front of ours {x + ship_size,y}")
                    return
            if x - 1 >= 0:#para evitar outofrange
                if self.table[x - 1][y] == 1:#se tem navio atras
                    print(f'there is a ship behind ours {x - 1,y}')
                    return
        else:
            #aqui verificacao navio na horizontal, [x][y + n]
            for i in range(ship_size):
                if self.table[x][y + i] == 1:#se tem navio exatamente na posicao escolhida
                    print(f'there is already a ship in {x,y + i}')
                    return
                if x + 1 < 10:
                    if self.table[x + 1][y + i] == 1:#se tem navio na linha de baixo
                        print(f"there is a ship below {x + 1,y + i}")
                        return
                if x - 1 >= 0:
                    if self.table[x - 1][y + i] == 1:#se tem navio na linha de cima
                        print(f"there is a ship on top{x - 1,y + i}")
                        return
            if y + ship_size < 10:
                if self.table[x][y + ship_size] == 1:#se tem navio na frecte, coluna da frente
                    print(f"there is a ship in front of ours {x,y + ship_size}")
                    return
            if y - 1 >= 0:
                if self.table[x][y - 1] == 1:#se tem navio atras
                    print(f'there is a ship behind ours {x,y - 1}')
                    return
        return True    
        
    def __fits_in_table(self,x,y,position,ship_size):
        if position == "horizontal":
            if y - 1 + ship_size > 9:#-1 porque incluimos a posicao inicial na contagem
                return False         #(1,5) + 5(size) *navio comeca na posicao 5 e acaba na 9. Dentro do range.
        else:
            if x - 1 + ship_size > 9:
                return False
            
        return True 
            
    def __get_valid_x_y(self):
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
    
    def __get_valid_position(self):
        while True:
            pos_input = input("horizontal(1) or vertical(2): ")
            if pos_input not in ['1','2']:
                print("invalid position(1 or 2)")
                continue
            elif pos_input == '1':
                return 'horizontal'
            else:
                return 'vertical' 
            
    def show_game_table(self):#mostra tabela principal
        print(' '*4,"0   1   2   3   4   5   6   7   8   9  ")
        for i,row in enumerate(self.game_table):
            print(i,end=" ")
            for col in row:
                print(f" | {col}",end="")
            print(' |\n','   ','-'*len(row)*4 + "-", sep='')
            
    def show_pretty_table(self):#mostra tabela principal
        print(' '*4,"0   1   2   3   4   5   6   7   8   9  ")
        for i,row in enumerate(self.table):
            print(i,end=" ")
            for col in row:
                print(f" | {' ' if col == 0 else 'X'}",end="")
            print(' |\n','   ','-'*len(row)*4 + "-", sep='')
            
    def ships_left(self):
        cont = 0
        for linha in self.table:
            cont += sum(linha)
        return cont