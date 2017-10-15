#!/usr/bin/python3

print()
print('+==================================================================+')
print('|                  ESTRUTURA DE DECISAO                            |')
print('|                  * IF  ELIF e ELSE *                             |')
print('+=====================================================TomJobs==v.1#+')
print()

idade = 19
autorizacao = True

if idade >= 18:
    print('Voce tem %s anos, já pode trabalhar.' %(idade))
elif idade == 17 and autorizacao is True:
    print('Você tem %s anos, mas tem autorização para trabalhar. ' %(idade))
else:
    print('Você não pode trabalhar!')