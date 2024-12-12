nome = input('Qual o seu nome: ')
print(f'O seu nome é {nome}')

#preciso converter pra fazer uma soma com números
#não é a maneira mais adequada
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

print(f'A soma do snúmeros é {num1 + num2}')

#maneira mais adequada, pois faz a verificação se foi digitado uma str
conv1 = int(num1)
conv2 = int(num2)

print(f'A soma do snúmeros é {conv1 + conv2}')
