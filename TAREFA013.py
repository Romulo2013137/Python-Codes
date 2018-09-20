preo = float(input('Qual é o preço do produto? R$'))
desconto = preo - (preo * 5 / 100)
print('O preço de R${:.2f} com desconto de 5% é R${:.2f} '.format(preo, desconto))
