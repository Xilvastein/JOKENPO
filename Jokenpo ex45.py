from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
escopc = randint(0,2)
print(''' Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*20)
print('Computador jogou {}!'.format(itens [escopc]))
print('Jogador jogou {}!'.format(itens[jogador]))
if escopc == 0: #PC jogou PEDRA
    if jogador == 0:
        print('\033[0;33mEMPATE!\033[0m')

    elif jogador == 1:
        print('\033[0;32mJogador venceu!\033[0m')

    elif jogador == 2:
        print('\033[0;34mComputador venceu!\033[0m')

    else:
        print('\033[0;31mJOGADA INVÁLIDA\033[0m')

elif escopc == 1: #PC jogou PAPEL
    if jogador == 0:
        print('\033[0;34mComputador venceu!\033[0m')

    elif jogador == 1:
        print('\033[0;33m EMPATE\033[0m')

    elif jogador == 2:
        print('\033[0;32mJogador Venceu!\033[0m')

    else:
        print('\033[0;31mJOGADA INVÁLIDA\033[0m')

elif escopc == 2: #PC jogou TESOURA
    if jogador == 0:
        print('\033[0;32mJogador Venceu!\033[0m')

    elif jogador == 1:
        print('\033[0;34mComputador Venceu!\033[0m')

    elif jogador == 2:
        print('\033[0;33mEMPATE\033[0m')

    else: print('\033[0;31mJOGADA INVÁLIDA\033[0m')

print('-='*20)

