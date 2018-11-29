s1 = str(input())
s2 = str(input())
print('Tamanho de {}: {}'.format(s1, len(s1)))
print('Tamanho de {}: {}'.format(s2, len(s2)))
if len(s1) != len(s2):
  print('A duas strings possuem diferentes tamanhos.')
if s1 != s2:
  print('As duas strings possuem conteúdos diferentes.')
