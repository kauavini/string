from random import choice
print('-=' * 13)
print('      JOGO DA FORCA')
print('-=' * 13)
palavras = ['chuva', 'osso', 'carro', 'caminhar', 'correr', 'tomar']
palavra = choice(palavras)
underline = ' _ '
str1 = ''
print('A palavra é : ')
tentativas = 1
indice = 0
while tentativas <= len(palavra):
    for i in range(len(palavra)):
        if palavra[i] in str1:
            print('{}'.format(palavra[i]), end='')
        else:
            print('{}'.format(underline), end='')
    chute = str(input(' Digite uma letra: '))
    if chute == '-1':
        print('Você venceu! ')
        break
    str1 += chute
    tentativas += 1
if tentativas == len(palavra):
    print('Suas tentativas acabaram :)')
