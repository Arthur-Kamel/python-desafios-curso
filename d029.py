c = {'ama' : '\033[93m',
     'fim' : '\033[m',
     'verm' : '\033[1;31m',
     'ver' : '\033[1;32m', }
v = float(input('Digite a sua velocidade de um carro em km/h: '))
if v > 80:
    print('{}O motorista ultrapassou o limite de 80 km/h e foi multado!{}'.format(c['verm'], c['fim']))
    multa = (v - 80) * 7
    print('{}Valor da multa: R$ {:.2f}{}'.format(c['ama'], multa, c['fim']))
else:
    print('{}O motorista respeitou o limite de 80km/h!{}'.format(c['ver'], c['fim']))
