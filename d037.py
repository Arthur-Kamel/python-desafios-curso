n = int(input('Digite um número inteiro qualquer: '))
print('[ 1 ] - Binário')
print('[ 2 ] - Octal')
print('[ 3 ] - hexadecimal')
r = int(input('escolha a base de conversão: '))
if r == 1:
    print('Valor em binário: {}'.format(bin(n)[2:]))
elif r == 2:
    print('Valor em octal: {}'.format(oct(n)[2:]))
elif r == 3:
    print('Valor em hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção inválida... tente novamente.')
print('Fim Programa')
