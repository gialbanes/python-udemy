entrada = input('[E]ntrar [S]air: ')
senha_digitda = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitda == senha_permitida:
    print('Entrar')
else:
    print('Sair')