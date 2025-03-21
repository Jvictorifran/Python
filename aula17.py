#operador or
#se qualquer valor for verdadeiro ele continua o codigo
entrada = input('[E]ntrar ou [S]air')
if entrada == 'E' or 'e':
  senha = input('digite a senha: ')
  if senha  == 'soupalmeiras' and entrada == 'E':
    print('bem vindo palmeiresne')
  else:
    print('senha errada')
else:
  print('voce saiu')

