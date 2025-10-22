def calculate_love_score(name1, name2):
    total_true = 0
    total_love = 0
    name1.lower()
    name2.lower()
    for letter in name1+name2:
        for i in 'true':
            if letter == i:
                total_true += 1
        for i in 'love':
            if letter == i:
                total_love += 1
    total_true = str(total_true)
    total_love = str(total_love)
    total = total_true + total_love
    print(f'Seu lovescore é de {total}%')
        
name1=input('Escreva o primeiro nome: ')
name2=input('Escreva o segundo nome: ')

calculate_love_score(name1,name2)

