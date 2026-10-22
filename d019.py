print('Qual aluno vai apagar o quadro?')

from random import choice
a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do último aluno: ')
print('O aluno selecionado(a) para apagar o quadro será: {}'.format(choice([a1,a2,a3,a4])))

