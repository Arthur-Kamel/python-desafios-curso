p = float(input('Digite o seu peso em quilo: '))
a = float(input('Digite o seu altura em metros: '))
icm = p/(a*a)
print('Pesando {}kg e medindo {}m o icm vale {:.2f}'.format(p, a, icm))
if p < 18.5:
    print('Status: abaixo do peso.')
elif p >= 18.5:
    print('status: peso ideal.')
elif p >= 25:
    print('status: Sobrepeso.')
elif p >= 30:
    print('status: Obesidade.')
elif p > 40:
    print('Status: obesidade mórbida.')