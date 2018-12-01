print('-='*  13)
print('    Validação de CPF')
print('-=' * 13)
cpf = str(input('Digite o cpf no formato xxx.xxx.xxx-xx: '))
if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    print('CPF válido')
else:
    print('CPF inválido')