#!/usr/bin/python3

print()
print('###################################################################')
print('#                  MANIPULAÇÃO DE ARQUIVOS                        #')
print('#                * Lê os dados em Arquivos *                      #')
print('#####################################################TomJobs##v.1##')
print()

#Lendo informações de um arquivo
print('Conteúdo do Arquivo:')
with open('Pythonize.txt', 'r') as f:
    print(f.read())    #Se não definir o local da inserção do texto, o mesmo sobrescreverá o conteúdo do arquivo.