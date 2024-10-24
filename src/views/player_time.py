def get_player_attack():
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

def display_player_turn():
    print("="*10)
    print("Sua vez de atacar!")
    print("="*10)
    

