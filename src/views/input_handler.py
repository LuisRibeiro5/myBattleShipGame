import random
random.seed(1)

class InputHandler:
    def get_player_attack(self):
        while True:
            try:
                x = input("Posição X (A-J): ").upper()
                x = ord(x) - ord("A")
                y = int(input("Posição Y (0-9): "))
                if 0 <= x < 10 and 0 <= y < 10:
                    return (x, y)
                else:
                    print("Coordenadas fora do limite!")
            except ValueError:
                print("Entrada inválida!")
    
    def get_enemy_attack(self):
        return (random.randint(0, 9), random.randint(0, 9))
    
    def get_valid_position(self):
        """Obtém uma posição válida do jogador para o posicionamento de um navio."""
        while True:
            try:
                x = input("Posição X (A-J): ").upper()
                x = ord(x) - ord("A")
                y = int(input("Posição Y (0-9): "))
                if 0 <= x < 10 and 0 <= y < 10:
                    return (x, y)
                else:
                    print("Coordenadas fora do limite! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Tente novamente.")
    
    def get_orientation(self):
        """Obtém a orientação do navio do jogador: horizontal ou vertical."""
        while True:
            orientation = input("Orientação (H para horizontal, V para vertical): ").upper()
            if orientation in ["H", "V"]:
                return "horizontal" if orientation == "H" else "vertical"
            else:
                print("Entrada inválida! Escolha 'H' para horizontal ou 'V' para vertical.")