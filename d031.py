d = float(input('digite a distância da viagem em KM: '))
if d <= 200:
    v = (d * 0.50)
    print('O valor da viagem Será: R$ {:.2f}'.format(v))
else:
    v = (d * 0.45)
    print('O valor da viagem será: R$ {:.2f}'.format(v))