r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if (r1+r2) >r3 and (r1+r3)>r2 and (r2+r3)>r1:
    print('É possível criar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é esquilátero')
    elif r1 != r2 != r3:
        print('O triângulo é escalêno')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('O triângulo é isósceles')
else:
    print('é impossível criar um triângulo.')
