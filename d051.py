print('10 Termos de um PA')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10) * r
for c in range(p, d, r):
    print ('{} '.format(c), end='-> ')
print('FIM')