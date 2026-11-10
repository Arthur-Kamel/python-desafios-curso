sd3 = 0
qtd = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        sd3 += c
        qtd += 1
print('A soma total entre os {} números divisíveis por 3: {}'.format(qtd, sd3))
