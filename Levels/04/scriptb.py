#!/usr/bin/python3

user = 'Pereira'
admin = False

def admin(funcao):    #funcao funcao
    def banana():    #recebe funcao
        print('Verificando se tem aceso %s' %funcao.__name__)
        global user
        global admin
        if user == 'Pereira':
            admin = True
        else:
            admin = False
        return funcao()
    return banana    #retorna uma funcao

@adm
def acesso_sistema():
    global admin
    if admin == True:
        print ('acesso permitido')
    else:
        print ('acesso negado!')
