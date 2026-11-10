sm = 0
ct = 0
for c in range(1, 7):
    n = int(input('Digite um valor inteiro: '))
    if n % 2 == 0:
        sm += n
        ct += 1
print('A soma de todos os {} números pares é igual a {}'.format(ct, sm))
