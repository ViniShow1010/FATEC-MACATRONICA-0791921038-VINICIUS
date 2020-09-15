#Pede para o usario digitar uma senha e valida ela com a senha secreta
#Cria uma variavel para uardar a senha
senha_secreta = '123456'

#Pede para o usuario digitar a senha senha_secreta
senha = input('Informe sua senha: ')

#Verifica se a senha esta correta
if senha == senha_secreta:
  print('Bem vindo Hackerman')
else:
  print('Acesso negado ')
