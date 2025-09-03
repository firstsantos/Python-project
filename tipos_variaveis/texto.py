# Declaração simples do tipo texto

nome_completo = "Gabriel Casemiro"

# Declaração de algo, mas que possa ser lido um abaixo do outro

nome_completo_aspas = """Gabriel
Casemiro"""

#Declaração com barra invertida, se enquadra na mesma funcionalidade da primeira 

nome_completo_quebra = "Gabriel \
Casemiro"



nome = "Gabriel"
sobrenome = "Casemiro"

# Formatação

print("Nome completo (1a forma):", nome_completo)

print("Nome completo (2a forma): " + nome_completo)

print("Nome completo (3a forma):" + " Gabriel " + "Casemiro ")

print("Nome completo (4a forma): " + "Gabriel", "Casemiro")

print("Nome Completo (5a forma):",nome_completo_aspas)

print("Nome Completo (6a forma):", nome_completo_quebra)

# É uma forma de formatação que substitui que requer o número de %
print("Nome Completo (7a forma): %s" % nome_completo)

# É possível fazer com mais de uma variavel, entretando, com o aumento, é necessário colocar entre parenteses
print("Nome Completo (8a forma): %s %s" % (nome, sobrenome) )

print(f"Nome Completo (9a forma): {nome} {sobrenome}")

print("Nome Completo (10a forma): {} {}".format(nome, sobrenome))