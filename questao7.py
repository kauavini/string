frase = str(input('Digite um frase: '))
qvogais = 0
qespacos = 0
vogais = 'aeiouAEIOUéÉÔôááÁÁ'
for i in range(len(frase)):
  if frase[i] == '':
    qespacos += 1
  if frase[i] in vogais:
    qvogais += 1
print(f'Existem {qespacos} espaços vazios.')
print(f'Existem {qvogais} vogais.')
