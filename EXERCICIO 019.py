import random
n1 = input('Primeiro aluno ')
n2 = input('Segundo aluno ')
n3 = input('terceiro aluno ')
n4 = input ('quarto aluno ')
escolhido = [n1, n2, n2, n3, n4]
sorteio = random.choice(escolhido)
print('O aluno sorteado é {} '.format(sorteio))
