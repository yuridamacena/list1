tamanho = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Velocidade da inernet em  (MBs): '))
    
print('Tempo aporximado de download: %.0f minutos' % (( tamanho / velocidade) * 60))
