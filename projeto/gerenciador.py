def adicionar_tarefa(tarefas, nome_tarefa):

    # tarefa: nome da tarefa 
    # completada: indicar se essa tarefa já foi completada ou não
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionado com sucesso!")
    return

tarefas = []

while True:
    print("\nMenu do gerenciador de tarefas")
    print("1. Adicionar uma tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha:") 

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar:")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "6": 
        break


    print("Programa finalizado")
