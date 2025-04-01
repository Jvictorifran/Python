# exec A
try: #if entrada.isdigit(): seria outra maneira
  numero = int(input('Digite um numero inteiro: '))
except:
  print('voce nao digitou um numero inteiro')

if numero % 2 == 0:
  print(f'o {numero} é par')
else:
  print(f"o {numero} é impar")

# exec B
dia = int(input("qual o horario? "))
try:
  if dia >= 0 and dia <= 11:
    print('Bom dia, meu amigo!')
  elif dia >= 12 and dia <= 17:
    print('Boa tarde, Meu amigo!')
  elif dia >= 18 and dia <= 23:
    print('Boa noite, bora tomar uma?')
  else: 
    print('isso não é uma Hora')
except:
  print('Digite um numero inteiro')

# exec C
nome = input('Digita seu nome: ')

if len(nome) <= 4:
  print('seu nome é pequeno')
elif len(nome) >= 5 and len(nome) <= 6:
  print('seu nome é normal')
elif len(nome) > 6:
  print('seu nome é gigante')
else:
  print('impossivel cair aqui')
