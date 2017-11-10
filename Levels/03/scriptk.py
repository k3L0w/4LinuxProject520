#!/usr/bin/python3

print()
print('--------------------------------------------------------------------')
print(':::::::::::::::::: MANIPULAÇÃO DE ARQUIVOS :::::::::::::::::::::::::')
print('::::::::::::::::::: LAÇO DE REPETIÇÃO FOR ::::::::::::::::::::::::::')
print('--------------------------------------------------------------------')
print()

animais = ['lion', 'fish', 'cat', 'dog', 'horse']

for animal in animais:
    if animal == 'horse':
        print("Animal: horse encontrado!")
        break   #This is command is Stop in program.
else:
    print("Animal: horse não encontrada.")