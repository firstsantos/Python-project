# excecoes são eventos que ocorrem durante a execucao do código, podendo interromper o funcionamento do programa se não forem tratadas


print("exemplo de captura de exceções")

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero
        print(f"resultado {resultado}")
    except ValueError as e:
        print(f"Erro de value error: {e}")
    except Exception as e:
        print(f"Erro: {e}")