#!/usr/bin/python3

#-*- coding: utf-8 -*-

###ATIVIDADE###

"""
# Criação de script para cadastrar entregas:
# 1 - Ele devera solicitar nome e sobrenome,
#     verificar se estes dados são do tipo string e gravar
#     isso em um arquivo chamado controle.txt com o padrão nome.sobrenome (minusculo)
# 2 - Após cadastrar o nome, solicite o número do cadastro, verifique se o número é do tipo inteiro e
#     grave isso num arquivo chamado número.txt
#      Caso eu digite 'q' nas duas primeiras perguntas, ele deve encerrar o programa
# Se a entrega for cadastrada com sucesso, posso cadastrar outra sem iniciar o novamente.
"""

while True:
    nome = input('Digite o seu nome: ')
    sobrenome = input('Insira sobrenome: ')

    if nome == 'q' and sobrenome == 'q':
        exit()

    elif type(nome) == str and type(sobrenome) == str:
        with open('controle.txt', 'a') as f:
            f.write('%s.%s' %(str.lower(nome), str.lower(sobrenome)))
            print('Remetente cadastrado \n')

            numero = int(input('Insira o número: '))
            if type(numero) == int:
                with open('numero.txt', 'a') as f:
                    f.write(str(numero))
                    print('Numero cadastrado com sucesso \n')