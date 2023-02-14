''' Programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa perguntará o VALOR DA CASA, o SALÁRIO do
comprador e em QUANTOS ANOS pagará.
O valor da prestação mensal será calculado, sabendo que esta não pode exceder
28% do salário ou então o empréstimo será negado. '''

emp = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Qual é o seu salário? R$ '))
anos = float(input('Em quantos anos pagará a casa? '))
mes = emp / (anos * 12)

print('Para comprar uma casa de R${:.2f} em {:.0f} anos ({:.0f} parcelas), a prestação será de R${:.2f}.'.format(emp, anos, anos*12, mes))
if mes <= (28/100) * sal:
    print('Seu empréstimo foi \033[1;34mAprovado!\033[m ')

else:
    print('Seu empréstimo foi \033[1;31mNegado.\033[m \nLamento!')



''' - As varáveis 'emp', 'sal' e 'anos' terão entradas de números decimais ou inteiros
    - A variável 'mes' quer dizer: mensalidade/parcela
    - Linha 10: a mensalidade é igual ao valor da casa dividido pelo total de meses/anos
    - Linha 12: digite o texto substituindo as {} e o que está dentro, pelas variáveis assinaladas respectivamente ao final
    - Linha 13: se a mensalidade for igual ou menor a 28% do salário, então leia a linha 14
    - Linha 16: se a linha 13 não for verdadeira leia a linha 17
    - Linhas 14 e 17: digite o texto lendo e aplicando as informações de formaração apresentadas
'''



