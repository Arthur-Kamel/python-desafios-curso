n = str(input('Digite algo: ')).strip().upper()
p = n.split()
j = ''.join(p)
i = j[::-1]
'''for c in range(len(j)-1, -1, -1):
    i += j[c]'''
print('{} invertido é {}'.format(j, i))
if i == j:
    print('É um palíndromo')
else:
    print('Não é um palindromo')
