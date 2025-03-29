# j o a o
# 0 1 2 3
# nome = 'João'
# print('Jo' in nome)
# print('zero' in nome)
# print(10* '-')
# print('Jo' not in nome)
# # print('zero' not in nome)
nome = input ('Digite seu nome: ')
encontrar = input('digite oque você quer encontrar: ')
print(100* '-')

if encontrar in nome:
  print(f'{encontrar} está em {nome}')
else:
  print(f'{encontrar}0 não está em {nome}')