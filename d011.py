print('='*20)
print('ÁREA DE PAREDES\n')
print('informe os valores em metros')
a = float(input('altura da parede: '))
l = float(input('largura da parede: '))

print('A area de uma parede com altura {:.2f} m e largura {:.2f} m vale {:.2f} m²'.format(a, l, a*l))
print('Litros de tinta necessários: {:.3f} L'.format((a*l)/2))
