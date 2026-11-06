p = float(input('Digite o seu peso em quilo: '))
a = float(input('Digite o seu altura em metros: '))
icm = p/(a*a)
print('Pesando {}kg e medindo {}m o icm vale {:.2f}'.format(p, a, icm))
if icm < 18.5:
    print('Status: Abaixo do peso')
elif 18.5 <= icm <= 25:
    print('Status: Peso normal')
elif 25 <= icm <= 30:
    print('Status: Sobrepeso')
elif 30 <= icm <= 40:
    print('Status: Obesidade')
else:
    print('Status: Obesidade mórbida')