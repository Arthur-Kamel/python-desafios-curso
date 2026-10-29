n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
m = (n1+n2)/2
print('Tirando {:.1f} e {:.1f} a média vale {:.1f}.'.format(n1, n2, m))
if m < 5:
    print('\033[31mAluno reprovado!\033[m'.format(m))
elif m <= 6.9 and m > 5:
    print('\033[93mO aluno está em recuperação.\033[m'.format(m))
elif m > 7:
    print('\033[32mAluno aprovado!\033[m'.format(m))
print('Fim do Programa.')
