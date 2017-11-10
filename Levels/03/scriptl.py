#!/usr/bin/python3

print()
print('--------------------------------------------------------------------')
print('::::::::::::::::::: ESTRUTURA DE REPETIÇÃO :::::::::::::::::::::::::')
print(':::::::::::::::::::        DESAFIO        ::::::::::::::::::::::::::')
print('--------------------------------------------------------------------')
print()

###ATIVIDADES###
#Crie um estrutura que contenha: nome e os cursos (que o aluno realizou(lista))    #dic.
#Solicite ao usuário que digite qual curso deseja buscar.
#Percorra a lista, encontre os usuarios que fizeram o curso digitado e mostre o nome do aluno.
#PS: TENHA AO MENOS 2 ALUNOS.

lista = [{'nome':'Antonio', 'cursos':['python','linux', 'SysAdmins']}, {'nome':'joao', 'cursos':['python','frontend']}, {'nome':'Geek', 'cursos':['games','3d']}]
nome = input('Digite o curso: ')
for item in lista:
    for curso in item['cursos']:
        if nome == curso:
            print (item['nome'])
