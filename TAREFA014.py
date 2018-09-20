salario = float(input('Qual é o salário do Funcionário? R$'))
almento = salario + (salario * 15 / 100)
print('O funcionário que ganha R${:.2f} com 15% de aumento, passa a ganhar R${:.2f}'.format(salario, almento))
