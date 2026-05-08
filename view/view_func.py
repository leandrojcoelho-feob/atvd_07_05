from controllers.controller import CinemaController

def exibir_menu_func():
    print("\n" + "="*45)
    print("--- PAINEL DO FUNCIONÁRIO ---")
    print("="*45)
    print("[1] Cadastrar um Cinema")
    print("[2] Cadastrar um Filme")
    print("[3] Criar uma Sessão")
    print("[4] Registrar Público em uma Sessão")
    print("[0] Voltar ao Menu Principal")
    print("="*45)

def menu_funcionario():
    controller = CinemaController()
    
    while True:
        exibir_menu_func()
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

        elif opcao == '0':
            print("\nSaindo do painel do funcionário...")
            break
        else:
            print("\n=> Opção inválida! Tente novamente.")