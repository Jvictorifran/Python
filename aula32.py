contador = 0
nome = input('Digite seu nome: ')

while contador < len(nome):
  print(f'{nome[contador]} é a {contador+1} letra do seu nome')
  contador += 1