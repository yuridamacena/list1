x = float(input('Digite o tamanho em metros quadrados: '))
litro = x/3

preço = 80
capacidade = 18

latas = litro / capacidade
total = latas * preço

print('Você usara ',latas,'latas de tintas: ')
print('O preço total e de: R$', total)