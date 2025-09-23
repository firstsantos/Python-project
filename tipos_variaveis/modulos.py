# São arquivos que contem definições e ações que podem ser reutilizadas por outros programas, tem múdulos que já vem do python e outros feitos por pessoas, mais especifico



print("Exemplo de importação de um módulo padrão:")

#import math
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"a raiz quadrada de 25 é {raiz_quadrada}")


print("\nExemplo de criação e utilização de um módulo personalizado")


from meu_modulo import saudacao, dobro

mensagem = saudacao("Gabriel")
resultado = dobro(5)

print(mensagem)
print(f"O dobro de 5 é: {resultado}")