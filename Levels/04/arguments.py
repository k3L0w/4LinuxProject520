#!/usr/bin/python3

# Teoria do *args / **kargs

print('')
print('*args -> Converte tudo em uma Tupla')
def add_user(*args):
    print(args)

if __name__ == '__main__':
    add_user('Pleta', 'Ude', 'Joao')

print()
#**kargs -> transforma tudo em um dicionario
print('**kargs -> convertendo tudo em um dicionário')
def add_user(**kwargs):
    print(kwargs['nome'])

if __name__ == '__main__':
    add_user(nome='Pereira', idade=20)