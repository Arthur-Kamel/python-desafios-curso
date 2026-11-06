from random import randint
from time import sleep
a = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
u = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*10)
print('''Escolha do Jogador {}
Escolha do computador {}'''.format(a[u], a[c]))
print('-='*10)
if c == 0:
    if u == 0:
        print('Empate')
    elif u ==1:
        print('Você venceu')
    elif u==2:
        print('Computador venceu')
    else:
        print('Jogada inválida')
elif c == 1:
    if u == 0:
        print('Computador venceu')
    elif u == 1:
        print('Empate')
    elif u == 2:
        print('Você venceu')
    else:
        print('Jogada inválida')
elif c == 2:
    if u == 0:
        print('Você venceu')
    elif u == 1:
        print('Computador venceu')
    elif u == 2:
        print('Empate')
    else:
        print('Jogada inválida')