tarefas = []

def adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return
    for tarefa in tarefas:
        print(f"\nNome: {tarefa['nome']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Categoria: {tarefa['categoria']}")
        print('-' * 30)

def concluir_tarefa(tarefas, nome):
    for tarefa in tarefas:
        if tarefa['nome'] == nome:
            tarefas.remove(tarefa)
            print(f"Tarefa '{nome}' concluída e removida!")
            return
    print(f"Tarefa '{nome}' não encontrada.")

def exibir_tarefas_por_prioridade(tarefas, prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'] == prioridade]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa com prioridade {prioridade}.")
        return
    for tarefa in tarefas_filtradas:
        print(f"Nome: {tarefa['nome']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Categoria: {tarefa['categoria']}")
        print('-' * 30)

def exibir_tarefas_por_categoria(tarefas, categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['categoria'] == categoria]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa na categoria '{categoria}'.")
        return
    for tarefa in tarefas_filtradas:
        print(f"Nome: {tarefa['nome']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print('-' * 30)

def menu():
    print("\nMenu de Comandos:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Exibir Tarefas por Prioridade")
    print("5. Exibir Tarefas por Categoria")
    print("6. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            nome = input("Nome da tarefa: ").capitalize()
            descricao = input("Descrição da tarefa: ").capitalize()
            prioridade = int(input("Prioridade (1-3): "))
            categoria = input("Categoria: ").capitalize()
            adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            nome = input("Nome da tarefa a ser concluída: ").capitalize()
            concluir_tarefa(tarefas, nome)
        elif escolha == '4':
            prioridade = int(input("Prioridade para filtrar (1-3): "))
            exibir_tarefas_por_prioridade(tarefas, prioridade)
        elif escolha == '5':
            categoria = input("Categoria para filtrar: ").capitalize()
            exibir_tarefas_por_categoria(tarefas, categoria)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
