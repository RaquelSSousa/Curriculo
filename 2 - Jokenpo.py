'''Programa em que o computador joga Jokenpô com o usuário.'''

from random import randint                                                   # importação das bibliotecas necessárias
from time import sleep

print('\033[7;30m*\033[m'*15, '\033[1;33mJOKENPÔ\033[m', '\033[7;30m*\033[m'*15)
itens = ['Pedra', 'Papel', 'Tesoura']                                        # lista de possíveis escolhas
pc = randint(0, 2)                                                           # o pc irá esolher ao acaso um item da lista
jogador = int(input('''Escolha:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual é a sua jogada? '''))                                                  # o usuário escolhe um item da lista

if jogador <= 2:                                                            # se o usuário escolher um número válido
    print('JO ', end='')
    sleep(1)                                                                # tempo de espera para ler a próxima linha
    print('KEN ', end='')
    sleep(1)
    print('PÔ!!!')
    sleep(1 / 3)
    print('-=-' * 11)
    print('O Computador escolheu \033[31m{}\033[m'.format(itens[pc]))       # digitar a escolha do pc
    print('O Jogador escolheu \033[36m{}\033[m'.format(itens[jogador]))     # digitar a escolha do usuário
    print('-=-' * 11)

    if jogador == 0:                                                        # se o usuário jogou Pedra
         if pc == 0:                                                        # e o pc jogou pedra digite a linha abaixo
            print('EMPATE')
         elif pc == 1:                                                      # se não, se, o pc jogou papel, digite a linha abaixo
            print('\033[31mCOMPUTADOR VENCE')
         elif pc == 2:                                                      # se não, se, o pc jogou tesoura, digite a linha abaixo
            print('\033[36mJOGADOR VENCE')
         else:                                                              # senão, digite a linha abaixo
            print('JOGADA INVÁLIDA!')
    elif jogador == 1:                                                      # se o usuário jogou Papel
         if pc == 0:
            print('\033[36mJOGADOR VENCE')
         elif pc == 1:
            print('EMPATE')
         elif pc == 2:
            print('\033[31mCOMPUTADOR VENCE')
         else:
            print('JOAGADA INVÁLIDA!')

    elif jogador == 2:                                                      # se o usuário jogou Tesoura
        if pc == 0:
            print('\033[31mCOMPUTADOR VENCE')
        elif pc == 1:
            print('\033[36mJOGADOR VENCE')
        elif pc == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA!')

else:                                                                       # se o jogador não escolher um número válido
    print('\033[1;7;47mJOGADA INVÁLIDA!\033[m')
