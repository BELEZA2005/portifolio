# RECEBENDO DADOS
from random import choice
print('VAMOS JOGAR!!')
print('SELECIONE UMA DAS OPÇÕES ABAIXO:')
print('AS OPÇÕES SÃO \n 1 = PEDRA  \n 2 = PAPEL  \n 3 = TESOURA')
# JOGADOR ESCOLHE
jogador = str(input('DIGITE UMA DAS OPÇÕES (1,2,3):'))
if jogador != '1' and jogador != '2' and jogador != '3':
    print('\033[31mOPÇÃO INVÁLIDA')
else:
    computador = choice(['1', '2', '3'])
    escolhas = {'1': 'PEDRA', '2': 'PAPEL', '3': 'TESOURA'}
    print(f'\033[32mVOCÊ JOGOU {escolhas[jogador]} E EU JOGUEI {escolhas[computador]}')
    # CONTINUAÇÃO
    if jogador == '1' and computador == '3' or jogador == '2' and computador == '3' or jogador == '3' and computador == '1':
        print('VOCÊ VENCEU')
    elif jogador == computador:
        print('DROGA EMPATAMOS')
    else:
        print('HEHEHE EU VENCI DESSA VEZ')















