vc = float(input('Digite o valor da casa: R$ '))
s = float(input('Digite o salário do comprador: R$ '))
a = float(input('Digite quantos anos deseja pagar: '))
pm =  vc/(a*12)
if pm > s*(30/100):
    print('Valor da prestação mensal: R$ {:.2f}. excedeu o valor de 30% do salário do comprador, que vale:{:.2f}.'.format(pm, s*(30/100)))
    print('\033[31mEmpréstimo negado.\33[m')
else:
    print('Valor da prestação mensal: R$ {:.2f}. Está abaixo do valor de 30% do salário do comprador, que vale:{:.2f}'.format(pm, s*(30/100)))
    print('\033[32mEmpréstimo aprovado.\33[m')
print('Fim do programa.')
