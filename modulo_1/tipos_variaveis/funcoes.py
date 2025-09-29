# Exemplo de função

def saudacao(nome):
    print(f"Olá!, {nome}!")


print("\nChamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")


# Funcao com retorno

def quadrado(numero):
    resultado =  numero ** 2
    return resultado 

print("\nChamando funcao quadrado:")
resultado_quadrado = quadrado(5)
print(f"Resultado da funcao quadrado:", resultado_quadrado)



# Chamar uma funcao com multiplos parametros

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a funcao soma:")
resultado_soma = soma(20, 50)
print("A soma do numero 20 e 50 é:", resultado_soma)



def soma(numero3, numero4):
    resultado = numero3 + numero4
    return resultado

print("\nSoma dos números abaixo:")
numero3 = 20
numero4 = 40
resultado_soma2 = soma(numero3, numero4)
print("O resultado do número %s e do número %s é %s" % (numero3, numero4, resultado_soma2))