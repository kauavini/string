numero = str(input('Digite seu número de telefone: '))
numero2 = ''
if len(numero) == 8:
    for i in range(0, len(numero)):
        if i == 0:
            numero2 += '3'
        else:
            numero2 += numero[i - 1]
print(numero2)
