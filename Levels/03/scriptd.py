#!/usr/bin/python3

print()
print('###################################################################')
print('#                  MANIPULAÇÃO DE ARQUIVOS                        #')
print('#                * Lê os dados em Arquivos *                      #')
print('#####################################################TomJobs##v.2##')
print()

#Lendo todas informações de um arquivo
with open('Pythonize.txt', 'r+') as f:
    print(f.read())