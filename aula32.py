# contador = 0
# nome = input('Digite seu nome: ')

# while contador < len(nome):
#   print(f'{nome[contador]} é a {contador+1} letra do seu nome')
#   contador += 1

nome = 'joao victor'
tamanho_str = len(nome)
contador = 0
nova_string = ''
while contador < tamanho_str:
  nova_string += '*' + nome[contador] + '*'
  print(nova_string)
  contador += 1