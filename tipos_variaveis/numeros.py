
# Inteiro
numero_inteiro = 3 
# exibição com a váriavel embutida
print ("Inteiro = ", numero_inteiro)


# Real com ponto flutuante
numero_real = 3.14
print("Real com ponto flutuante = ", numero_real)



# type() - comando que lhe mostra qual class é passada na variavel
print("Tipo da variavel inteiro = ", type(numero_inteiro))


print("Tipo da variavel real = ",type(numero_real))


# soma + 

soma = 1 + 1
print("1 + 1 = ", soma)

# subtração - 

subtracao = 1 - 1
print("1 - 1 = ", subtracao)

# multiplicação *

multiplicacao = 2 * 2
print("2 x 2 = ", multiplicacao )

# divisao /

divisao = 5 / 2
print("5 / 2 = ", divisao)
print("Tipo da variavel de divisao = ", type(divisao))
#  int() - realiza a ação de arredondar o número se for maior 0.5 para cima, caso seja menor ou igual 0.5 ele arredonda para baixo 
print("Valor em inteiro = ", int(divisao))


# float() - realiza a ação de tranformação um número que é inteiro em real com o 0.0

print("Valor em float = ", float(divisao))

# Modulo % - haveria dois modos de interpretar esse operador, o primeiro seria esse abaixo, que resulta no resto da dívisão,
# apesar de não parecer ele já usa o float entendendo que o resto é um número real acima do 0.5, arredondando para 2

modulo = 5 % 3
print("Modulo = ", modulo)

# Divisao inteiro // - 

divisao1 = 5 // 2
print(" 5 // 2 = ", divisao1)
print ("Tipo da variavel do resultado da divisao = ", type(divisao1))