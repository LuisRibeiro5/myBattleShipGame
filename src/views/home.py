def display_home_menu():
    import os
    print("="*10, "Batalha Naval", "="*10)
    print("1.\t Iniciar Jogo")
    print("2.\t sair")
    resp = input("> ")
    
    if resp == "2":
        exit()
    elif resp == "1":
        return
    else:
        print("Escolha uma opcao 1/2")
        os.system('cls' if os.name == 'nt' else 'clear')
        display_home_menu()