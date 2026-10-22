from datetime import date
an = int(input('Em que ano o jovem nasceu: '))
aa = date.today().year
age = aa - an
print('O jovem tem {} anos de idade.'.format(age))
if age < 17:
    print('Ele ainda irá se alistar ao serviço militar.')
elif age >= 17 and age == 18:
    print('É hora de se alistar.')
elif age > 18:
    print('Já se passou o tempo do alistamento.')
