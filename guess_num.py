import random

# definir número gabarito
n = random.randint(1, 100)

resp = 0

counter = 0

while resp != n:
    resp = int(input('Adivinhe o número (entre 1 e 100): '))
    counter += 1
    if resp > n:
        print("Muito alto! Tente de novo")
    elif resp < n:
        print("Baixo demais! Tente de novo")
    elif resp == n:
        print(f"Parabéns! Você adivinhou o número em {counter} tentativas")
        break
    else:
        print("Resposta inválida")
