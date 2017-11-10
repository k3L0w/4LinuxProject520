#!/usr/bin/python3

#-*- coding? utf-8 -*-

###DESAFIO###
#1. Criar uma classe chamada Carro
# ela deve ter os atributos: velocidade máxima de 180 e velocidade atual (zero)
# criar um método para frear, ele deve verificar a velocidade atual, se for maior do que zero, abaixar a velocidade. Se for igual a zero, mostrar que o carro já está parado.

class Carro:
    vel_max = 180
    vel_atual = 0

    def acelerar(self):
        acel = int(input('Quanto deseja acelerar: '))
        if acel > self.vel_max:
            print('ATENTION!!!')
            print('VELOCIDADE EXCESSIVA!')
        elif self.vel_atual < self.vel_max and acel <= self.vel_max:
            self.vel_atual += acel
            if self.vel_atual > self.vel_max:
                print('ATENÇÃO! Velocidade não permitida')
            else:
                print('Velocidade permitida, boa viagem!', self.vel_atual)
        else:
            print('Você atingiu o limite de velocidade')

    def frear(self):
        acel = int(input('Quanto deseja frear:'))
        if self.vel_atual > 0:
            self.vel_atual -= acel
            if self.vel_atual < 0:
                print('Você não pode frear tudo isso!!!')
            else:
                print('Velocidade atual: ', self.vel_atual)
        elif self.vel_atual == 0:
            print('O carro está parado')

if __name__ == '__main__':
    carro = Carro()
    while True:
        opcao = int(input('Digite 1 para ACELERAR ou 2 para FREAR: '))
        if opcao == 1:
            carro.acelerar()
        elif opcao == 2:
            carro.frear()
        else:
            print('Opção INVÁLIDA!')

