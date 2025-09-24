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
        print(f"{indice}. [{status}] {contato}")

def favoritar_contato(agendas, indice_contato):
    indice_contato_favoritado = int(indice_contato) - 1
    if not agendas[indice_contato_favoritado]["salvo"]:
        agendas[indice_contato_favoritado]["salvo"] = True
        print("Contato favoritado :)")
    else:
        agendas[indice_contato_favoritado]["salvo"] = False
        print("Contato desmarcado como favorito :(")

    return

def atualizar_contato(agendas, indice_contato, nova_agenda):
    indice_contato_atualizado = int(indice_contato) - 1
    if indice_contato_atualizado >= 0 and indice_contato_atualizado <= len(agendas):
        agendas[indice_contato_atualizado]["agenda"] = nova_agenda
        print(f"Contato{indice_contato} atualizado para {nova_agenda}")
    else:
        print("Índice de tarefa inválido.")
    return

def ver_contatos_favoritos(agendas):
    print("\nContatos favoritos: ")
    for indice, agenda in enumerate(agendas, start=1):
        if agenda["salvo"]:
            print(f"{indice}. {agenda['agenda']}")

def apagar_contato(agendas):
    for agenda in agendas:
        if agenda["salvo"]: 
            agendas.remove(agenda)
    print("Agenda removida com sucesso.")
    return

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
        contato = input("Digite o contato na ordem; nome, telefone, email: ")
        adicionar_contato(agendas, contato)
    elif escolha == "2":
        ver_contatos(agendas)
    elif escolha == "3":
        ver_contatos(agendas)
        indice_contato = input("Digite o contato que deseja marcar/desmarcar como favorito: ")
        favoritar_contato(agendas, indice_contato)
    elif escolha == "4":
        ver_contatos(agendas)
        indice_contato = input("Escolha a agenda que deseja atualizar:")
        nova_agenda = input("Digite o novo nome da agenda: ")
        atualizar_contato(agendas, indice_contato, nova_agenda)
    elif escolha == "5":
        ver_contatos_favoritos(agendas)
    elif escolha == "6":
        ver_contatos(agendas)
        indice_contato = input("Selecione o contato a ser removido: ")
        apagar_contato(agendas)
    elif escolha == "7":
        break
    