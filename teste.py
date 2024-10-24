# navio = {"posicao":[(1,2),(1,3),(1,4)]}
# x,y = navio["posicao"][0]
# print((x,y) in navio["posicao"])

# print(all(navio["posicao"]))
# i = 0
# while True:
#     navio["posicao"][i] = input("k: ").upper()
    
#     print(all(navio["posicao"]))
#     if all(ship == "X" for ship in navio["posicao"]):
#         print("navio destruido")
#         break
#     i += 1

def set_positions(initial_pos, size, orientation):
    positions = {}
    x,y = initial_pos

    for i in range(size):
        if orientation == "vertical":
            positions[ (x + i,y) ] = True
        else:#Horizontal
            positions[ (x,y + i) ] = True

    return positions

if __name__ == "__main__":
    positions = set_positions((0,0), 5, "vertical")
    print(positions)
    for pos in positions:
        print(pos, type(pos))
    print(all([ positions.values()]))