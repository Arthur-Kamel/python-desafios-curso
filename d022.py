n = input('Nome: ')
nmm = n
n = n.split()
print(nmm.upper())
print(nmm.lower())
print('Seu nome tem ao todo {} letras'.format(len(''.join(n))))
print('Seu primeiro nome é {} e tem {} letras.'.format(n[0], len(n[0])))