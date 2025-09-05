#É uma coleção de elementos ordenaveis e mutaveis

# Declaração de uma lista

minha_lista = [1, 2, 12, 3, 51, 4, 5, 6, 7, 8 ,9 , 112]


# minha_lista [0] = "python"

# Exibindo a lista 
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista
print("minha_lista[0]:", minha_lista[0])

print("minha_lista[5]:", minha_lista[5])

print("minha_lista[1:7]:", minha_lista[1:7])

print(minha_lista[:6])

print(minha_lista[2:])


# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("minha_lista(6):", minha_lista)


# Metódo index

indice = minha_lista.index(6)
print("Indice do elemento 6: ", indice)



# Método insert: Insere um elemento em um índice específico 

minha_lista.insert(2, 10)
print("Após o insert(2, 10): ", minha_lista)


# Método pop 

elemento_removido = minha_lista.pop(3)
print("Elemento removido: ", minha_lista)
print("Após pop(3):", minha_lista)


# Método remove 

minha_lista.remove(10)
print("Após remove(10):", minha_lista)


# Método sort

minha_lista.sort()
print("Após sort()", minha_lista)