# Jogo da velha


tab = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def tabuleiro():
    for i in range(3):
        print(f" {tab[i][0]} | {tab[i][1]} | {tab[i][2]}")  # [i]=linha
        if i < 2:
            print('---+---+---')



def definir_vencedor():
    for i in range(3):
        if tab[i][0] == 'X' and tab[i][1] == 'X' and tab[i][2] == 'X':
            print('Fim de jogo!\nO jogador X venceu!')
            return False
        elif tab[i][0] == 'O' and tab[i][1] == 'O' and tab[i][2] == 'O':
            print('Fim de jogo!\nO jogador O venceu!')
            return False
        elif tab[0][i] == 'O' and tab[1][i] == 'O' and tab[2][i] == 'O':
            print('Fim de jogo!\nO jogador O venceu!')
            return False
        elif tab[0][i] == 'X' and tab[1][i] == 'X' and tab[2][i] == 'X':
            print('Fim de jogo!\nO jogador X venceu!')
            return False
        elif tab [0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X':
            print('Fim de jogo!\nO jogador X venceu!')
            return False
        elif tab [0][2] == 'O' and tab[1][1] == 'O' and tab[2][0] == 'O':
            print('Fim de jogo!\nO jogador O venceu!')
            return False
        elif tab [0][0] == 'O' and tab[1][1] == 'O' and tab[2][2] == 'O':
            print('Fim de jogo!\nO jogador X venceu!')
            return False
        elif tab [0][2] == 'X' and tab[1][1] == 'X' and tab[2][0] == 'X':
            print('Fim de jogo!\nO jogador O venceu!')
            return False

lugares_ocupados=[]

def jogada(jogador):
    global lugares_ocupados
    while True:
        print(f"\nVez do jogador {jogador}:")
        jogada_linha = int(input("Escolha a linha (0-2): "))
        jogada_coluna = int(input("Escolha a coluna (0-2): "))

        # Guarda a posição (linha, coluna) como tupla
        localizacao = (jogada_linha,jogada_coluna)

        print(lugares_ocupados)
        if localizacao not in lugares_ocupados:
            tab[jogada_linha][jogada_coluna] = jogador
            lugares_ocupados.append(localizacao)
            break
        else:
            print("Esse lugar está ocupado, escolha outro")

        
        

print('Vamos jogar jogo da velha!')

for rodada in range(9):

    jogador = 'O' if rodada % 2 == 0 else 'X'

    jogada(jogador)
   
    tabuleiro()


    if definir_vencedor() == False:
        break

else:
    ('\nEmpate! O tabuleiro está cheio')
    

