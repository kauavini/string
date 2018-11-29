data = str(input('Data de nascimento: '))
mes = data[3:5]
if mes == '01':
  mes = 'Janeiro'
if mes == '02':
  mes = 'Fevereiro'
if mes == '03':
  mes = 'Março'
if mes == '04':
  mes == 'Abril'
if mes == '05':
  mes = 'Maio'
if mes == '06':
  mes = 'Junho'
if mes == '7':
  mes = 'Julho'
if mes == '8':
  mes = 'Agosto'
if mes == '9':
  mes = 'Setembro'
if mes == '10':
  mes = 'Outubro'
if mes == '11':
  mes = 'Novembro'
if mes == '12':
  mes = 'Dezembro'
print('Você nasceu em {} de {} de {}'.format(data[0:2], mes, data[6:10]))
