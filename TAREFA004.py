n = input('Digite algo')
print('O tipo primitivo do que foi digitado é ', type(n))
print('O que foi digitado é um espaço(s)?', n.isspace())
print('O que foi digitado contem apenas números?', n.isnumeric())
print('O que foi digitado contem apenas letras?', n.isalpha())
print('O que foi digitado contem letras e números?', n.isalnum())
print('O que foi digitado está apenas em maiúsculo(a)(s)?', n.isupper())
print('O que foi digitado está apenas em minúsculo(a)(s)?', n.islower())
print('O que foi digitado é um título?', n.istitle())
