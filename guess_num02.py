import random

min = int(input("Diga o valor mínimo: "))
max = int(input("Diga o valor máximo: "))
chances = int(
    input("Em quantas tentativas você garante que consegue acertar? "))

print(f"Você tem {chances} chances")

n = random.randint(min, max)

resp = 0

counter = 0

while True:

    if counter > chances:
        print('Suas chances acabaram!')
        break

    resp = int(input(f'Adivinhe o número (entre {str(min)} e {str(max)}): '))
    if resp > n:
        print("Muito alto! Tente de novo")
        counter += 1
    elif resp < n:
        print("Baixo demais! Tente de novo")
        counter += 1
    elif resp == n:
        print(f"Parabéns! Você adivinhou o número em {counter} tentativas")
        break
    else:
        print("Resposta inválida")



# Qual era o trabalho de ontem?nn vai ter trabalho mais ele falou, oq ele mostrou era só uma atividade, tem atividade hoje? faz só quem quiser, ta no drive aquilo ali, shooow
