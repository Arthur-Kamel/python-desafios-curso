from random import randint
from time import sleep
c = {'magen' : '\033[35m',
     'verde' : '\033[1;92m',
     'vermelho' : '\033[1;91m',
     'azul' : '\033[1;94m',
     'fim' : '\033[m',
     'amarelo' : '\033[1;93m',}
n = randint(1,5)
print('{}-=-{}'.format(c['magen'], c['fim'])*11)
print('{}Qual o número pensei entre 0 e 5?{}'.format(c['amarelo'], c['fim']))
print('{}-=-{}'.format(c['magen'], c['fim'])*11)
r = int(input('Resposta: '))
print('{}PROCESSANDO'.format(c['amarelo']), end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
if r == n:
    print('Escolhi {}. {}Você acertou!{}'.format(n, c['verde'], c['fim']))
else:
    print('Escolhi {}. {}Você errou!{}'.format(n ,c['vermelho'], c['fim']))
