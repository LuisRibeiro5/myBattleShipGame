from src.runtime import Runtime

def test_initialize_ships():
    game = Runtime()
    game.initialize_ships(game.player_table)
    game.initialize_ships(game.enemy_table)
    game.test()

def test_handle_enemy_turn():
    run = Runtime()
    run.handle_enemy_turn()
    
def test_handle_player_turn():
    run = Runtime()
    run.handle_player_turn()

def test_starts_ships():
    run = Runtime()
    run.start_ships()
    run.test_print_boards()

def test_start():
    run = Runtime()
    run.start_game()

def test():
    run = Runtime()
    run.test_print_boards()

if __name__ == "__main__":
    test_start()