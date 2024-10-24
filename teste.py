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

positions = {}

positions[1,2] = False

print(positions)

