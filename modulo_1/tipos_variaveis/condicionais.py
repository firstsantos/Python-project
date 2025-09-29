# if, elif e else

#Deixar a pergunta dinamica
#Tranformando em inteiro

idade = int(input("Quantos anos você tem? "))
print("Exemplo de comando if---------")


if idade >= 18:
 print("Você é maior de idade.")



if idade == 19:
 print("Você tem 19 anos")


if idade < 18:
 print("Você é menor de idade.")

 

if idade != 10:
  print("Você não tem 10 anos")




print("Exemplo de comando else ---------------")

if idade >= 19:
  print("Você é maior de idade.")
else:
 print("Você não tem menos que 19 anos.")




 print("exemplo de elif")

if idade >= 18:
  print("Você é maior de idade")
elif idade >= 12:
  print("Você é um adolescente")
else:
  print("Você é menor de idade")

 

print("Mais exemplos ----------------")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você Não pode tirar a carteira de habilitação" #Forma de colocar o comando em apenas uma linha.

print(mensagem)



