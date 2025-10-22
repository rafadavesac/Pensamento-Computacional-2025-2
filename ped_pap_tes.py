import random
import emoji

ped= emoji.emojize(":rock:")
pap=emoji.emojize(":page_facing_up:")
tes=emoji.emojize(":scissors:")

lista = [ped, pap, tes]
comp = random.choice(lista)

continuar='s'

while continuar == 's':
    user= input("Pedra, papel ou tesoura? ").lower()

    if user=='papel' and comp==ped:
        print(f'Você escolheu {pap}')
        print(f'O computador escolheu {ped}')
        print('Você ganhou!') 
    elif user=='papel' and comp==tes:
        print(f'Você escolheu {pap}')
        print(f'O computador escolheu {tes}')
        print('Você perdeu!')
    elif user=='papel' and comp==pap:
        print(f'Você escolheu {pap}')
        print(f'O computador escolheu {pap}')
        print('Empate!')

    elif user=='tesoura' and comp==ped:
        print(f'Você escolheu {tes}')
        print(f'O computador escolheu {ped}')
        print('Você perdeu!') 
    elif user=='tesoura' and comp==tes:
        print(f'Você escolheu {tes}')
        print(f'O computador escolheu {tes}')
        print('Empate!')
    elif user=='tesoura' and comp==pap:
        print(f'Você escolheu {tes}')
        print(f'O computador escolheu {pap}')
        print('Você ganhou!')

    elif user=='pedra' and comp==ped:
        print(f'Você escolheu {ped}')
        print(f'O computador escolheu {ped}')
        print('Empate!') 
    elif user=='pedra' and comp==tes:
        print(f'Você escolheu {ped}')
        print(f'O computador escolheu {tes}')
        print('Você ganhou!')
    elif user=='pedra' and comp==pap:
        print(f'Você escolheu {ped}')
        print(f'O computador escolheu {pap}')
        print('Você perdeu!')

    else:
        print('Resposta inválida')

    continuar=input('Continuar? (s/n) ').lower()
print('Obrigado por jogar!')

