import random

#Não finalizei

counter=0
result=[]
while True: 
    resp = input("Jogar dado? (s/n) ")
    if resp.lower() == "s":
        dados = int(input("Quantos dados deseja jogar? "))
        counter= counter + 1
        for n in range(dados):
            result.append(random.randint(1,6))
        print(f"Os resultados dos dados jogados são: {result}")
        result=[]
    elif resp.lower()=="n":
        print("Nem queria jogar mesmo :(")
        print(f"Você jogou dados {counter} vezes")
        break
    else:
        print("Resposta inválida")
