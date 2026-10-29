from datetime import date
aa = date.today().year
an = int(input('Digite o ano de nascimento: '))
age = aa - an
print('Com nascimento em {}, a idade é {} em {}'.format(an, age, aa))
if age <= 9:
    print('A Categoria é Mirim.')
elif age <= 14:
    print('A Categoria é Infantil.')
elif age <= 19:
    print('A categoria é Junior.')
elif age <= 25:
    print('A categoria é Senior.')
else:
    print('A categoria é master.')