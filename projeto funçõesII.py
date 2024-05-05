
opcoes_tarefas = ["adicionar tarefas", "listar tarefas", "marcar tarefas como concluídas"]

def adicionar_tarefa(opcoes_tarefas):
    entrada = input("Digite a sua tarefa: ")
    opcoes_tarefas.append(entrada)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(opcoes_tarefas):
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(opcoes_tarefas, 1):
        print(f"{i}. {tarefa}")

escolha_tarefas = int(input('Faça sua escolha: adicionar tarefas (1), listar tarefas (2) ou marcar tarefas como concluídas (3): '))

if escolha_tarefas == 1:
    adicionar_tarefa(opcoes_tarefas)
elif escolha_tarefas == 2:
    listar_tarefas(opcoes_tarefas)
elif escolha_tarefas == 3:
    pass
else:
    print("Escolha inválida.")
    
    #Ambiente Virtual, seguem comandos:
#1) python3 -m venv myenv;
#2) myenv\Scripts\activate;
#3) python seu_script.py;


