v = float(input('Digite o valor do produto: R$'))
print('''Selecione a forma de pagamento
[1] À vista(10% de desconto)
[2] À vista no cartão(5% de desconto)
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão''')
r = int(input('Digite a opção: '))
if r == 1:
    print('O valor a ser pago será R${:.2f} com um desconto de 10%'.format(v-v*0.1))
elif r == 2:
    print('O valor a ser pago será R${:.2f} com um desconto de 5%'.format(v-v*0.05))
elif r == 3:
    print('''Sua compra será parcelada em {} vezes com o valor de R${:.2f} sem juros
A sua compra de R${:.2f} Vai ter o seu valor mantido.'''.format(2, v / 2, v))
elif r == 4:
    v2 = v+v*0.2
    p = int(input('Quantidade de parcelas: '))
    print('''Sua compra será parcelada em {} vezes com o valor de R${:.2f} com juros.
A sua compra de R${:.2f} Vai custar R${:.2f} no final.'''.format(p, v2/p, v, v2))
else:
    print('Opção invalida!')