# Jogar dado (s/n):
# Caso n seja s/n: print('expressao invalida)
# jogar dado : s -> (dois numeros de 1 a 6 aleatorios)
# jogar dado n: -> Jogo encerrado

import random  # permite a função random (gera valores aleatórios)

# Minha tentativa
# x=True
# while x==True:
#     resp = input("Jogar dado? (s/n) ")
#     if resp.lower() == "s":
#         n1=random.randint(1,6)
#         n2=random.randint(1,6)
#         print(f"({n1},{n2})")
#     elif resp.lower()=="n":
#         print("Nem queria jogar mesmo :(")
#         x=False
#     else:
#         print("Resposta inválida")


# Maneira melhor
while True:
    resp = input("Jogar dado? (s/n) ")
    if resp.lower() == "s":
        n1 = random.randint(1, 6)
        n2 = random.randint(1, 6)
        print(f"O primeiro dado deu {n1} e o segundo deu {n2}")
    elif resp.lower() == "n":
        print("Nem queria jogar mesmo :(")
        break
    else:
        print("Resposta inválida")
