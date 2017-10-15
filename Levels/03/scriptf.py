#!/usr/bin/python3

#-*- coding: utf-8 -*-

print()
print('###################################################################')
print('#                  MANIPULAÇÃO DE ARQUIVOS                        #')
print('#                  * DESAFIO - LEVEL 03 *                         #')
print('#####################################################TomJobs##v.1##')
print()

# -------------------------------------------------------------------------
# - DESAFIO LEVEL 03:                                                     -
# -------------------------------------------------------------------------
# O Usuário deve digitar:
# . o nome do remetente;
# . do destinatário;
# . Produto
# . Previsão de entrega.
#
# Obs.: TODAS ESSAS INFORMAÇÕES DEVERÃO SER GRAVADAS EM ARQUIVO.
# -------------------------------------------------------------------------

#VARIÁVEIS
remetente = input('Insira o nome do remetente: ')
destinatario = input('Insira o nome do destinatário: ')
produto = input('Insira o produto: ')
previsao = input('Insira a previsão de entrega: ')

with open('Cadastro.txt', 'a') as f:
    f.write('\nRemetente: %s - Destinatario: %s - Produto: %s - Previsao: %s' %(remetente, destinatario, produto, previsao))

#Cadastro de 5 entregas e exiba a quarta entrega
with open('Cadastro.txt','r') as f:
    print(f.readlines())

print()
print('--------------------------------------------------------------------')
print("            CADASTRO DE PRODUTO EFETUADO COM SUCESSO                ")
print('--------------------------------------------------------------------')