import random
import emoji

# Ask user to make a choice
# If choice is not valid
#   print an error
# Let the computer make a choice
# Print the choices (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
#   terminate the program

# Dictionary: is used to map a key to a value | key -> value
# 'r' -> emoji.emojize(":rock:")

emojis = {'r':emoji.emojize(":rock:"),'p':emoji.emojize(":page_facing_up:"),'s':emoji.emojize(":scissors:")} #Dicionário

# -> é uma tupla, uma 'lista' imutável, 'read only', não dá p/ alterar ela no meio do código
choices = ('r', 'p', 's')



computer_choice = random.choice(choices)


while True:
    user_choice = input('Rock, paper or scissors? (r/p/s): ').lower()

    if user_choice not in choices:
        print('Invalid choice!')

    print(f"You chose {emojis[user_choice]}")
    print(f"The computer chose {emojis[computer_choice]}")

    if computer_choice == user_choice:
        print("It's a tie!")
    elif computer_choice == 'r' and user_choice == 'p':
        print('you won!')
    elif computer_choice=='p' and user_choice=='s':
        print('You won!')
    elif computer_choice=='s' and user_choice=='r':
        print('You won!')
    else:
        print('You lost :(')

    continuar=input("Continue playing? (y/n): ")
    if continuar !='y':
        print('Thanks for playing!')
        break

    
    
#agora ta bem menor o código kkkk
    #Sim, vamos desenhar? Onde? O pedra, papel, tesoura mto trabalho nn tenho essa habilidade tem sim, poxaaaa, me da mais um hehe
    #eu to vendo essa aula td de novo ;-;
    # No YT? nn, ele ta repetindo tudo oq ele falou ontem, puts, mas aprendeu bem? kkk ss - Eu vi isso no ensino medio que chique - que tortura realmente
