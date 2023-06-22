quanto_ganha = float(input('Quanto ganha por hora? '))
horas_trabalhadas = int(input('Horas trabalhadas por mês '))
salario_bruto = quanto_ganha * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.88
sindicato = salario_bruto * 0.05


print('+ Salário Bruto : R$ %.2f' % salario_bruto )

print('-IR: R$ %.2f' % ir )

print('-inss: R$ %2f' % inss )

print('-Sindicato: R$ %.2f ' %sindicato )

print('= Salário liquido : R$ %.2f' %(salario_bruto - ir - inss - sindicato))