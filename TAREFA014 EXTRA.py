preo = float(input('Digite o preço do produto: R$'))
desconto = preo - (preo * 20 / 100)
juros = preo + (preo * 15 / 100)
print('Este produto custa R${:.2f}: a vista você terá 20% de desconto R${:.2f}. a prazo ele terá 15% de juros R${:.2f}'.format(preo, desconto, juros))
