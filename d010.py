print('='*20)
print('CONVERSOR MONETÁRIA\n')
nr = float(input('Valor em reais que você possui: R$ '))
d = nr / 5.12
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(nr, d))

