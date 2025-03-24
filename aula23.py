"""
 Exercício
 Peça ao usuário para digitar seu nome
 Peça ao usuário para digitar sua idade
 Se nome e idade forem digitados:
     Exiba:
         Seu nome é {nome}
         Seu nome invertido é {nome invertido}
         Seu nome contém (ou não) espaços
         Seu nome tem {n} letras
         A primeira letra do seu nome é {letra}
         A última letra do seu nome é {letra}
 Se nada for digitado em nome ou idade: 
     exiba "Desculpe, você deixou campos vazios."
 """

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
print(100*'-')

if nome and idade != '':
  print(f'seu nome é {nome}')
  print(f'seu nome de tras para frente é {nome[::-1]}')
  if ' ' in nome:
    print ('seu nome tem espaço!')
  else:
    print('seu nome nao tem espaço')
  print(f'seu nome contem {len(nome)} letras')
  print(f'sua inicial é {nome[0]}')
  print(f'sual ultima letra é {nome[len(nome)-1]}')
else:
  print('você deixou campos vazios')