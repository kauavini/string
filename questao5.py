nome = str(input('Digite o seu nome: '))
ultimaletra =  len(nome)
while ultimaletra >= 0:
  if ultimaletra == len(nome):
    print(nome[:ultimaletra])
  else:
    print(nome[:ultimaletra])
  ultimaletra -= 1
