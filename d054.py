from datetime import date
pma = 0
pmn = 0
an = 0
aa = date.today().year
for c in range(1, 7):
    an = int(input('Digite a o ano de nascimento da {}° pessoa:'.format(c)))
    age = (aa-an)
    if age >= 18:
        pma += 1
    else:
        pmn += 1
print('''
Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas maiores de idade'''.format(pma, pmn))
