data = str(input('Data de nascimento: '))
mes = data[3:5]
if mes[0] == '0'
print(mes)
meses = 'Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'
meses = meses.split()
print('Você nasceu em {} de {} de {}'.format(data[0:2], mes, data[6:10]))
