import os
import time

class DisplayManager:
    def show_welcome(self):
        self.print_ship_animation()
        print("=" * 10, "Batalha Naval", "=" * 10)
    
    def display_home_menu(self):
        """Exibe o menu inicial com opções para iniciar o jogo ou sair."""
        while True:
            self.clear_screen()
            print("\n=== Menu Principal ===")
            print("1. Iniciar Jogo")
            print("2. Sair")
            choice = input("Escolha uma opção (1/2): ")
            if choice == "1":
                return "start"
            elif choice == "2":
                exit()
            else:
                print("Opção inválida. Escolha novamente.")
                time.sleep(1)
    
    def display_positioning_menu(self):
        """Exibe o menu de posicionamento com opções para escolher posicionamento manual ou aleatório."""
        self.clear_screen()
        while True:
            print("\n=== Posicionamento de Navios ===")
            print("1. Posicionar Minhas Peças")
            print("2. Posicionar Aleatoriamente")
            choice = input("Escolha uma opção (1/2): ")
            if choice == "1":
                return "manual"
            elif choice == "2":
                return "random"
            else:
                print("Opção inválida. Escolha novamente.")
                time.sleep(1)
    
    def display_positioning_screen(self, board, input_handler, ship_name, ship_size):
        """Exibe a tela de posicionamento com instruções e tabuleiro lado a lado."""
        self.clear_screen()
        
        # Obter as linhas de instruções
        instruction_lines = self.get_instruction_lines(ship_name, ship_size)
        
        # Obter as linhas do tabuleiro
        board_lines = self.format_board(board.grid)
        
        # Determinar o número máximo de linhas entre instruções e tabuleiro
        max_lines = max(len(instruction_lines), len(board_lines))
        
        # Preencher listas com linhas vazias se necessário
        while len(instruction_lines) < max_lines:
            instruction_lines.append("")
        while len(board_lines) < max_lines:
            board_lines.append("")
        
        # Definir espaçamento entre instruções e tabuleiro
        spacing = "    "  # 4 espaços
        
        # Imprimir linhas combinadas
        for instr, board_line in zip(instruction_lines, board_lines):
            print(f"{instr.ljust(40)}{spacing}{board_line}")
    
    def get_instruction_lines(self, ship_name, ship_size):
        """Retorna as linhas de instruções para o posicionamento do navio."""
        instructions = [
            f"=== Posicionando o {ship_name} ===",
            f"Tamanho do navio: {ship_size}",
            "",
            "Escolha a posição inicial do navio:",
            "- Para X, insira uma letra entre A-J.",
            "- Para Y, insira um número entre 0-9.",
            "",
            "Escolha a orientação do navio:",
            "- H para horizontal",
            "- V para vertical",
        ]
        return instructions
    
    def show_invalid_position(self):
        """Informa ao jogador que a posição é inválida."""
        print("Posição inválida. Tente novamente.")
        time.sleep(1)
    
    def display_player_board(self, board):
        """Exibe o tabuleiro do jogador no lado direito."""
        print("\n" + " " * 35 + "Seu Tabuleiro")
        board_lines = self.format_board(board.grid)
        for line in board_lines:
            print(" " * 35 + line)
            
    def get_positioning_input(self, ship_name, ship_size, input_handler):
        """Obtém as entradas de posicionamento do jogador."""
        # Coletar posição X e Y
        position = input_handler.get_valid_position()
        x, y = position[0], position[1]
        
        # Coletar orientação
        orientation = input_handler.get_orientation()
        
        return (x, y, orientation)
    
    def print_ship_animation(self):
        navio = [
            "              |    |    |",
            "             )_)  )_)  )_)",
            "            )___))___))___)\\",
            "         ____|____|____|____\\___",
            "---------\\                   /---------",
            "  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^",
            "    ^^^^      ^^^^     ^^^    ^^",
            "         ^^^^      ^^^"
        ]
        steps = 30
        for step in range(steps):
            os.system('cls' if os.name == 'nt' else 'clear')
            for line in navio:
                print(" " * step + line)
            time.sleep(0.04)
    
    
    def format_board(self, grid, hide_ships=False):
        """Formata o tabuleiro para exibição, ocultando navios se `hide_ships` for True."""
        board_lines = ["  " + "   ".join(map(str, range(len(grid))))]
        for i, row in enumerate(grid):
            row_str = chr(i + 65) + " " + " | ".join(
                [" " if cell == "S" and hide_ships else cell for cell in row]
            )
            board_lines.append(row_str)
        return board_lines
    
    def show_turn(self, player):
        self.clear_screen()
        if player == "Player":
            print("\n" + "=" * 15 + " Sua Vez! " + "=" * 15)
        else:
            print("\n" + "=" * 15 + " Vez do Inimigo " + "=" * 15)
    
    def show_boards(self, player_board, enemy_board):
        """Exibe os tabuleiros lado a lado."""
        title_width = 27
        player_title = "Seu Tabuleiro".center(title_width)
        enemy_title = "Tabuleiro do Inimigo".center(title_width)

        print(f"\n{player_title}        {enemy_title}\n")
        
        player_lines = self.format_board(player_board.grid)
        enemy_lines = self.format_board(enemy_board.grid, hide_ships=True)
        
        for player_line, enemy_line in zip(player_lines, enemy_lines):
            print(f"{player_line}        {enemy_line}")
    
    def show_hit(self, player, msg = ""):
        if msg: print(f"{player} {msg}!")
        else: print(f"{player} acertou um navio!")
        time.sleep(1)
    
    def show_miss(self, player):
        print(f"{player} errou!")
        time.sleep(1)
    
    def show_winner(self, winner):
        print(f"\n{winner} venceu o jogo!")
        exit()
    
    def clear_screen(self):
        """Limpa a tela, dependendo do sistema operacional."""
        os.system('cls' if os.name == 'nt' else 'clear')