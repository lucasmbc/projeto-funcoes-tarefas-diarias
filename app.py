tarefas = {}
lista_tarefas = set()

def adicionar_tarefa(dicionario, chave, valor):
    dicionario[chave] = valor

def listar_tarefas(lista):
    print(lista)

controlador = ""

while(controlador != "sair"):
    tarefa = input("\nDigite uma tarefa: ")
    adicionar_tarefa(tarefas, "Tarefa", tarefa)
    lista_tarefas.add(tarefas["Tarefa"])

    opcoes = input("\nOpções: \n\t'a' adicionar nova tarefa \n\t'l' exibir lista de tarefas \n\t's' sair: \n")
    if(opcoes == "s"):
        controlador = "sair"
        print("\nPrograma encerrado.")
    elif opcoes == "l":
        listar_tarefas(lista_tarefas)
