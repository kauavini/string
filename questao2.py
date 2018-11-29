nome = str(input('Digite seu nome: '))
ultimaletra = len(nome) - 1
nomerevertido = ''
while ultimaletra >= 0:
  nomerevertido += nome[ultimaletra]
  ultimaletra -= 1
print(nomerevertido.upper())
