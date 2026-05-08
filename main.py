from controllers.controller import CinemaController
from repository.repository import DatabaseSetup

def exibir_menu():
    print("\n" + "="*45)
    print("--- SISTEMA DE GESTÃO DE CINEMAS ---")
    print("="*45)
    print("[1] Cadastrar um Cinema")
    print("[2] Cadastrar um Filme")
    print("[3] Criar uma Sessão")
    print("[4] Registrar Público em uma Sessão")
    print("-" * 45)
    print("[5] Consultar apenas Cinemas")
    print("[6] Consultar apenas Filmes")
    print("[7] Consultar Sessões (Geral / Detalhado)")
    print("[8] Consultar Sessões de um Cinema Específico")
    print("-" * 45)
    print("[0] Sair do Sistema")
    print("="*45)

def menu_principal():
    DatabaseSetup.initialize()
    controller = CinemaController()
    
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            print("\n--- Cadastro de Cinema ---")
            nome = input("Nome do cinema: ")
            try:
                capacidade = int(input("Capacidade de público: "))
                endereco = input("Endereço completo: ")
                sucesso, msg = controller.cadastrar_cinema(nome, capacidade, endereco)
                print(f"\n=> {msg}")
            except ValueError:
                print("\n=> ERRO: A capacidade deve ser um número! Operação cancelada.")

        elif opcao == '2':
            print("\n--- Cadastro de Filme ---")
            titulo = input("Título do filme: ")
            try:
                duracao = int(input("Duração (em minutos): "))
                diretor = input("Diretor: ")
                genero = input("Gênero: ")
                sucesso, msg = controller.cadastrar_filme(titulo, duracao, diretor, genero)
                print(f"\n=> {msg}")
            except ValueError:
                print("\n=> ERRO: A duração deve ser um número! Operação cancelada.")

        elif opcao == '3':
            print("\n--- Criação de Sessão ---")
            try:
                cinema_id = int(input("ID do Cinema: "))
                filme_id = int(input("ID do Filme: "))
                data_hora = input("Data e Hora (ex: 10/05 20:00): ")
                sucesso, msg = controller.criar_sessao(cinema_id, filme_id, data_hora)
                print(f"\n=> {msg}")
            except ValueError:
                print("\n=> ERRO: Os IDs devem ser números! Operação cancelada.")

        elif opcao == '4':
            print("\n--- Registro de Público ---")
            try:
                sessao_id = int(input("ID da Sessão: "))
                cinema_id = int(input("ID do Cinema (para validação): "))
                publico = int(input("Quantidade de público presente: "))
                sucesso, msg = controller.registrar_publico(sessao_id, cinema_id, publico)
                print(f"\n=> {'SUCESSO' if sucesso else 'ERRO'}: {msg}")
            except ValueError:
                print("\n=> ERRO: Valores inválidos digitados!")

        elif opcao == '5':
            print("\n--- Lista de Cinemas ---")
            cinemas = controller.listar_cinemas()
            if not cinemas: print("Nenhum cinema cadastrado.")
            for c in cinemas:
                print(f"ID: {c.id} | Nome: {c.nome} | Capacidade: {c.capacidade} | Endereço: {c.endereco}")

        elif opcao == '6':
            print("\n--- Lista de Filmes ---")
            filmes = controller.listar_filmes()
            if not filmes: print("Nenhum filme cadastrado.")
            for f in filmes:
                print(f"ID: {f.id} | Título: {f.titulo} | Duração: {f.duracao}m | Gênero: {f.genero}")

        elif opcao == '7':
            print("\n--- Todas as Sessões Detalhadas ---")
            sessoes = controller.listar_sessoes()
            if not sessoes: print("Nenhuma sessão cadastrada.")
            for s in sessoes:
                print(f"Sessão ID: {s['sessao_id']} | Local: {s['cinema']} | Filme: {s['filme']} | Quando: {s['data_hora']} | Público: {s['publico']}")

        elif opcao == '8':
            print("\n--- Sessões por Cinema ---")
            try:
                cid = int(input("Digite o ID do Cinema que deseja consultar: "))
                sessoes = controller.listar_sessoes(cinema_id=cid)
                if not sessoes: 
                    print("Nenhuma sessão encontrada para este cinema.")
                for s in sessoes:
                    print(f"Sessão ID: {s['sessao_id']} | Filme: {s['filme']} | Quando: {s['data_hora']} | Público: {s['publico']}")
            except ValueError:
                print("\n=> ERRO: O ID do cinema deve ser um número!")

        elif opcao == '0':
            print("\nEncerrando o sistema... Até logo!")
            break
        
        else:
            print("\n=> Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()