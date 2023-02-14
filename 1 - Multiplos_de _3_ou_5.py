'''Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9.
A soma desses múltiplos é 23.
Encontre a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.'''

s = 0
count = 0
for c in range(1, 1000):
    if c % 3 == 0 or c % 5 == 0:
        count += 1
        s += c

print('A soma de todos os múltiplos de 3 ou 5 abaixo de 1000 é {}.'.format(s))

''' - Variável  's'      quer dizer: soma 
    - Variável  'count'  quer dizer: contagem
    - Linha 7:  para cada número (c) dentro do limite de 1 a 999, faça:
    - Linha 8:  se o número (c) for divido por 3 e tiver resto igual a 0, e se o número (c) for divido por 5 e tiver resto igual a 0
    - Linha 9:  o contador será igual ao contador + 1
    - Linha 10: a soma será igual a soma + 1
    - Linha 12: Escreva o texto adicionando no lugar das {} o valor de s (soma)
'''
