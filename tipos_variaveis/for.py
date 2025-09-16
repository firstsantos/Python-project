# É uma estrutura de permite que possamos repetir um bloco de código, caso o resultado seja verdadeiro, tornando assim, a ação repetitiva enquanto um valor for aquele


lista = [1, 2, 3, 4, 5]


print("for utilizando lista")
for elemento in lista:
    print(elemento)

    tupla = (1, 2, 3, 4, 5)


print("for utilizando tupla")
for elemento in tupla:
    print(elemento)



pessoa  = {"nome": "João", "idade": 30, "cidade": "Manaus"}
print("\nFor utilizando dicionario - chaves")

for chaves in list(pessoa.keys()):
    print(chaves)



print("\nFor utilizando dicionario - values")
for valor in pessoa.values():
    print(valor)


print("\nFor utilizando dicionario - valores")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")



#range(): intevalo númerico
#[0,1,2,3,4,5,6,7,8,9]

print("\nUtilizando a função range()")

range(0,10)

print(list(range(0,10)))

for numero in range(5):
    print("Número:", numero)




#len, a função len vai retornar a quantidade de itens que temos na lista


print("\nUtilizando a função range() com len()")

lista = [1, 2, 3, 4, 5]

print(lista)
for indice in range(0, len(lista)):
 if indice == 3:
    lista[indice] = 5
 else:
    lista[indice] = 0
print(lista)



# enumerate(), vai permitir que você use uma lista


lista_enumerate = ["a", "b", "c"]

for indice, valor in enumerate(lista_enumerate):
   print(f"{indice}: {valor}")
   if indice == 1:
      print("Indice 1")