#Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").

senha = input('Escreva sua senha: ')

if senha == 'python123':
    print('Parabens sua senha está correta')
else:
    print('Senha incorreta')