# Poo, é basicamente um paradguima de programação que se baseia na organização do programa em torno de objetos


# Classe exemplo:
class Pessoa:
    #quando definido com none, mostra que esse método não retorna nada
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


# Objetos, é uma instância da classe, criado apartir daquela classe, respeitando atributos e métodos

pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Rodrigo", 32)
mensagem = pessoa2.saudacao()
print(mensagem)
