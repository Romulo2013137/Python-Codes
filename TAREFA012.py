l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
d = (l*a)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, a, d))
tinta = d / 2
print('Para pintar essa parede é necessário {}l de tinta.'.format(tinta))
