#Adicionar contato

def adicionar_contato(agendas, contato):
    agenda = {"agenda": contato, "salvo": False}
    agendas.append(agenda)
    print(f"Contato:{contato}, adicionado com sucesso")
    return

def ver_contatos(agendas):
    print("\nLista de contatos:")
    for indice, agenda in enumerate(agendas, start=1):
        status = "✓" if agenda["salvo"] else " "
        contato = agenda["agenda"]
        print(f"{indice}. [{status}] ({contato})")

def favoritar_contato(agendas, indice_contato):
    indice_contato_favoritado = int(indice_contato) - 1
    agendas[indice_contato_favoritado]["salvo"] = True
    print("Contato favoritado :)")
    return

def atualizar_contato(agendas, indice_contato, novo_nome_agenda):
    print("Contato atualizado com sucesso!")

agendas = []

while True:
    print("\nMenu da Agenda.")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Favoritar contato")
    print("4. Editar contato")
    print("5. Contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha:")

    if escolha == "1":
        contato = input("Digite o contato na ordem; nome, telefone, email e se é favorito: ")
        adicionar_contato(agendas, contato)
    elif escolha == "2":
        ver_contatos(agendas)
    elif escolha == "3":
        ver_contatos(agendas)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contato(agendas, indice_contato)
    elif escolha == "4":
        ver_contatos(agendas)
        nova_agenda = input("Escolha uma agenda para atualizar: ")
        atualizar_contato(agendas, indice_contato)
    elif escolha == "7":
        break
    