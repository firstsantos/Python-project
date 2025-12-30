# Personagem: classe mãe , tudo que é comum entre os outros 
# Heroi: controlado pelo usuario
# inimigo: adversario do usuário

class Personagem:

    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome 
        self.__vida = vida
        self.__nivel = nivel


    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhe(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhe(self):
        return f"{super().exibir_detalhe()}\nHabilidade: {self.get_habilidade()}\n"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhe(self):
        return f"{super().exibir_detalhe()}\nTipo: {self.get_tipo()}\n"
    
heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
print(heroi.exibir_detalhe())
Inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")
print(Inimigo.exibir_detalhe())


