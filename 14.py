x = float(input('peso dos peixes por dia:'))

y = 50

z = None

multa = None

if x > y:

    z = x-y

    multa = z*4

    print('Você pagara multa por exceder o valor')

else:
    print('Você não pagara multa pois esta dentro do limite')