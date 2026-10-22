print('revelando seno, cosseno e tangente de um angulo')
from math import sin, cos, tan, radians
angulo = int(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno, cosseno e tangente de {}º é {:.2f}, {:.2f} e {:.2f}'.format(angulo, seno, cosseno, tangente))