import random
# Jogo da Forca

# Definir uma lista de palavras
palavras = ['morango', 'serrote', 'palavra']
resposta = random.choice(palavras)
erros = 0

print('Vamos jogar forca!')

print('Você tem 6 tentativas!')

tentativas_anteriores = []

comprimento_palavra = '_'*len(resposta)

print(comprimento_palavra)

forca = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

while True:

    tentativa = input('\nDiga uma letra: ')

    if tentativa in resposta:
        index = resposta.find(tentativa)
        comprimento_palavra = comprimento_palavra[:index] + \
            tentativa + comprimento_palavra[index+1:]

        print(forca[erros])
        print("\nBoa escolha!")
        tentativas_anteriores += tentativa

        palavra_list = list(comprimento_palavra)

        for i, letra in enumerate(resposta):
            if letra == tentativa:
                palavra_list[i] = tentativa
        comprimento_palavra = ''.join(palavra_list)
        print(comprimento_palavra)
    else:
        erros += 1
        print(forca[erros])
        print('\nEssa letra não está na palavra :(\n')
        print(comprimento_palavra)
        print(f"Você tem {6 - erros} tentativas restantes.")

   # if tentativa in tentativas_anteriores:
       # print("Você já adivinhou essa letra")

    if comprimento_palavra == resposta:
        print("\nParabéns! Você adivinhou a palavra!")
        break

    elif erros >= 6:
        print("Você perdeu!")
        break
