from datetime import date
an = int(input('Em que ano o jovem nasceu: '))
aa = date.today().year
age = aa - an
print('Quem nasceu em {}, tem {} anos de idade em {}.'.format(an, age, aa))
if age == 18:
    print('O indivívuo deve se alistar urgentemente.')
elif age < 18:
    saldo = 18 - age
    print('Ainda falta {} anos para se alistar'.format(saldo))
elif age > 18:
    saldo = age - 18
    print('Já passou {} anos para se alistar'.format(saldo))
    print('Seu alistamento foi em {}'.format(an+18))