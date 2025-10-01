# Herança 

#  exemplo:

print("\n Exemplo da herança: ")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass
        
# Reaproveitamento de classes em outras, visto que possuem a mesma ação
# Mas podem ser alteradas dependendo da situação

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    


dog = Cachorro(nome="Rex")

cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")