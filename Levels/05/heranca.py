#!/usr/bin/python3

#-*- coding: utf-8 -*-

#Respectivamente, arquivo e classe sendo importados.
from ClassePai import ClassePai

class ClasseFilho(ClassePai):

    def __init_(self):
        print("Acessando a Hierarquia filho.")

classe = ClasseFilho()
classe.metodo()
