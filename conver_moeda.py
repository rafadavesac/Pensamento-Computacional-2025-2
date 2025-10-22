# Convertor de moeda

#Valor que deseja converter
valor_inicial=float(input("Insira o valor: "))

#Moeda original
moeda_inicial=input('Moeda atual (BRL/EUR/USD): ').upper()

#Moeda final
moeda_final=input('Moeda desejada (BRL/EUR/USD): ').upper()

def frase_conversao():
    print(f"{valor_inicial:.2f} {moeda_inicial} é igual a {conversao:.2f} {moeda_final}.")


if moeda_inicial== 'BRL' and moeda_final == 'EUR':
    conversao= valor_inicial//6.25
    frase_conversao()

elif moeda_inicial== 'BRL' and moeda_final == 'USD':
    conversao= valor_inicial//5.32
    frase_conversao()

elif moeda_inicial== 'EUR' and moeda_final == 'BRL':
    conversao= valor_inicial*6.25
    frase_conversao()

elif moeda_inicial== 'EUR' and moeda_final == 'USD':
    conversao= valor_inicial*1.16
    frase_conversao()

elif moeda_inicial== 'USD' and moeda_final == 'EUR':
    conversao= valor_inicial//1.16
    frase_conversao()

elif moeda_inicial== 'USD' and moeda_final == 'BRL':
    conversao= valor_inicial*5.32
    frase_conversao()
