n = int(input('Digite um número inteiro: '))
d = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[93m{} \033[m'.format(c), end='')
        d += 1
    else:
        print('\033[31m{} \033[m'.format(c), end='')
print('')
print('O número {} foi divisível {} vezes.'.format(n, d))
if d == 2:
    print('Portanto, é um número primo.')
else:
    print('Portanto, não é um número primo.')
