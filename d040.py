n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('\033[31mA média vale: {}. Aluno reprovado!\033[m'.format(m))
elif m <= 6.9 and m > 5:
    print('\033[93mA média vale: {}. O aluno está em recuperação.\033[m'.format(m))
elif m > 7:
    print('\033[32mA média vale: {}. Aluno aprovado\033[m!'.format(m))
print('Fim do Programa.')