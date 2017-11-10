#!/usr/bin/python3

#-*- coding: utf-8 -*-

class Servidor(objeto):

    def contratar_memoria(self, memoria):
        self.memoria += memoria

    def contratar_disco(self, disco):
        self.disco += disco

    def contratar_cpu(self, cpu):
        self.cpu += cpu

#SERVIDOR CLOUD
class Cloud(Servidor):

    def __init__(self):    #Irá utilizar os dados da Class Servidor..
        self.memoria = 512
        self.cpu = 1
        self.disco = 100

        self.memoria = 1024
        self.cpu = 1
        self.disco = 100

#CONTRATACAO DE SERVIDOR
servidor = Cloud()
print('CPU atual: ', servidor.cpu)
print('Disco atual: ', servidor.disco)
servidor.contratar_cpu(1)
servidor.contratar_disco(100)
print('CPU novo: ', servidor.cpu)
print('Disco novo: ', servidor.disco)


class Fisico(Servidor):
    def __init__(self):
        self.memoria = 4096
        self.cpu = 4
        self.disco = 1024
        self.total_slots = 4
        self.slots_ocupados = 1

    def contratar_disco(self, disco):    #Poliformismo, duas classes contratar_discos, porém com métodos diferentes.
        if self.total_slots > self.slots_ocupados:
            self.slots_ocupados += 1
            self.disco += disco
        else:
            print ('Voce nao tem mais slots disponiveis')
            print ('Total de slots: ',self.total_slots)
            print ('Total ocupados: ',self.slots_ocupados)

        def contratar_convencional(self):
            super().contratar_disco(disco)

servidor = Fisico()
#print ('Disco atual: ',servidor.disco)
#servidor.contratar_disco(1024)
#print ('Disco novo: ',servidor.disco)
servidor.contratar_convencional(1024)
print ('Disco novo: ',servidor.disco)


