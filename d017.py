print('Revelando o valor da hipotenusa')
from math import hypot
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o segundo cateto: '))
hptn = hypot(c1, c2)
print('O valor da hipotenusa de um triangulo com dois lados medindo {} e {} é igual a {:.2f}'.format(c1, c2, hptn))