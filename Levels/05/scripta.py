#!/usr/bin/python3

##Classes e Métodos##

###ATIVIDADE###

#Objetivo
#Passe duas notas para o método prova da classe aluno (n1 e n2).
#Verifique a media, se o aluno tirou 5 ou mais, foi aprovado na materia caso contrario ele reprovou.


class Aluno():
    nome = "Antonio Pereira"
    email = "janaina@del.com.br"

    def prova(self, n1, n2):
        media = (n1 + n2) / 2
        if media >= 5:
            response = 'O(a) aluno(a) %s passou com a nota %s' %( self.nome, media)
        else:
            response = 'O(a) aluno(a) %s reprovou com a nota %s' % (self.nome, media)
        return response

if __name__ == '__main__':
    joao = Aluno()
    print(joao.prova(9,9))
print()