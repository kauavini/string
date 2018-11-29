nome = str(input('Digite o seu nome: '))
qletras = 0
for i in range(len(nome)):
  if i == 0:
    print(nome[qletras])
  else:
    print(nome[:qletras + 1])
  qletras += 1
