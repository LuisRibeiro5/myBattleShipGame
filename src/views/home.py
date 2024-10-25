def display_home_menu():
    print("=== Batalha Naval ===")
    print("1. Iniciar Jogo")
    print("2. sair")
    resp = input("> ")
    
    if resp == "2":
        exit()
    elif resp == "1":
        return
    else:
        print("Escolha uma opcao 1/2")
        display_home_menu()