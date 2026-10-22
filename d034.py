cor = {'limpa':'\033[m',
         'ver':'\033[32m',
         'mag':'\033[35m',
         'verm':'\033[91m',
         'ama':'\033[93m',
         'azu':'\033[34m'}
s = float(input('Digite o valor do salário: R$ '))
if s <= 1250:
    s = s + (s*0.15)
    print('O salário foi reajustado para {}R$ {:.2f}{} com aumento de {}15%{}'.format(cor['ver'], s, cor['limpa'], cor['azu'], cor['limpa']))
else:
    s = s + (s*0.10)
    print('O salário foi reajustado para {}R$ {:.2f}{} com aumento de {}10%{}'.format(cor['ver'], s, cor['limpa'], cor['azu'], cor['limpa']))
print('FIM')