print('TRABALHANDO UMA STRING\n{}'.format('='*22))
n = input('Digite algo: ')
print('O tipo primitivo de {} é '.format(n),type(n))
print('{} pode ser numérico? '.format(n),n.isnumeric())
print('{} pode ser alfabético?'.format(n),n.isalpha())
print('{} pode ser alfanumérico?'.format(n),n.isalnum())
print('{} é string em letra maiúsculo'.format(n), n.isupper())
print('{} pode ser um número decimal?'.format(n), n.isdecimal())


