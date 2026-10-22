cor = {'limpa':'\033[m',
         'ver':'\033[32m',
         'mag':'\033[35m',
         'verm':'\033[91m',
         'ama':'\033[93m',
         'azu':'\033[34m'}
print('{}+-{}'.format(cor['ama'], cor['limpa'])*11)
print('{}|  FORMA TRIÂNGULO? |{}'.format(cor['mag'], cor['limpa']))
print('{}+-{}'.format(cor['ama'], cor['limpa'])*11)
reta1 = float(input('Digite o valor da reta {}1{}: '.format(cor['azu'], cor['limpa'])))
reta2 = float(input('Digite o valor da reta {}2{}: '.format(cor['azu'], cor['limpa'])))
reta3 = float(input('Digite o valor da reta {}2{}: '.format(cor['azu'], cor['limpa'])))
if reta1 + reta2 > reta3 and reta3+reta2 > reta1 and reta3+reta1 > reta2:
    print('{}É possível criar um triângulo.{}'.format(cor['ver'], cor['limpa']))
else:
    print('{}NÂO é possível criar um triângulo.{}'.format(cor['verm'], cor['limpa']))
print('FIM DO PROGRAMA')