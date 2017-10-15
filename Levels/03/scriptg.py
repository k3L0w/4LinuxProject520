#!/usr/bin/python3

print()
print('###################################################################')
print('#                  MANIPULAÇÃO DE ARQUIVOS                        #')
print('#                * Acessando itens da lista *                     #')
print('#####################################################TomJobs##v.1##')
print()

#Acessando itens da lista -> File: Cadastro.txt)
with open ('Cadastro.txt', 'r') as f:
    x = f.readlines()
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
    print(x[4])
    print(x[5])
