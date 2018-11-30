str1 = str(input())
str2 = str1.split()
str2 = ''.join(str2)
str3 = []
for i in range(len(str2) - 1, 0 - 1, -1):
  str3.append(str2[i])
str3 = ''.join(str3)
if str2 == str3:
  print('Palíndromo')
else:
  print('Não é')
