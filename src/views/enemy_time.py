import random

def get_enemy_attack():
    while True:
        try:
            x = random.randint(ord('A'),ord('J'))
            y = random.randint(0,9)
            x = x - ord("A")#converte para idx da row
            if x < 0 or x >= 10:
                print("choose a x between 0 - 9")
                continue
            if y < 0 or y >= 10:
                print("choose a y between 0 - 9")
                continue
            break
        except:
            print("posicao invalida")
            
    return (x,y)

def display_enemy_turn():
    print("="*19)
    print("ATAQUE DO INIMIGO")
    print("="*19)