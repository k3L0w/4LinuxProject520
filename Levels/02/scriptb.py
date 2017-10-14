#!/usr/bin/python3

print()
print('  ###################################################################')
print('  #                 * ENTRADA E SAÍDA DE DADOS *                    #')
print('  #                         * Input *                               #')
print('  #####################################################TomJobs##v.1##')
print()

#Interação com o usuário
print()
print('- Olá, me chamo Ude!')
print('- Por favor insira as informações solicitadas abaixo!')

firstname = input('  Digite seu primeiro nome:  ')
lastname = input('  Digite seu último nome: ')
idade = input('  Digite o ano do seu nascimento: ')

#Exibindo os dados ao usuário
print()
print('  ###################################################################')
print("  Seu nome é", firstname, lastname )
print("  Você tem ou fará: %s anos" %(2017 - int(idade)))
print()
print('  Obrigado por fornecer as informações solicitadas, até a próxima, by!')
print('  ###################################################################')