# @classmethod
# @staticmethod


class MinhaClasse:
    valor = 10 # Atributo de classe
    
    def __init__(self, nome) -> None:
        self.nome = nome # Atributo da instância

    # requer umainstância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Metódo de classe chamado para valor={cls.valor}"

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())  # dessa forma é possível buscar o método
# print(MinhaClasse.metodo_instancia()) # dessa forma não é possível, sendo puxado diretamente da classe
print(MinhaClasse.valor) # Também é possível, já que não precisa de uma instância para acessar um atributo da classe
print(MinhaClasse.metodo_classe())