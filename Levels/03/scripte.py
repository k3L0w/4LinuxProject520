#!/usr/bin/python3

print()
print('###################################################################')
print('#                  MANIPULAÇÃO DE ARQUIVOS                        #')
print('#                * Acessando itens da lista *                     #')
print('#####################################################TomJobs##v.1##')
print()

#Acessando itens da lista
with open('Pythonize.txt', 'r') as f:
    x = f.readlines()
    print(x[0])
    print(x[1])