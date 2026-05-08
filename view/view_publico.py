from controllers.controller import CinemaController

def exibir_menu_publico():
    print("\n" + "="*45)
    print("--- ÁREA DO PÚBLICO (CONSULTAS) ---")
    print("="*45)
    print("[1] Consultar Cinemas")
    print("[2] Consultar Filmes em Cartaz")
    print("[3] Ver Todas as Sessões")
    print("[4] Ver Sessões de um Cinema Específico")
    print("[0] Voltar ao Menu Principal")
    print("="*45)

def menu_publico():
    controller = CinemaController()
    
    while True:
        exibir_menu_publico()
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            print("\n--- Lista de Cinemas ---")
            cinemas = controller.listar_cinemas()
            if not cinemas: print("Nenhum cinema cadastrado.")
            for c in cinemas:
                print(f"ID: {c.id} | Nome: {c.nome} | Endereço: {c.endereco}")

        elif opcao == '2':
            print("\n--- Lista de Filmes ---")
            filmes = controller.listar_filmes()
            if not filmes: print("Nenhum filme cadastrado.")
            for f in filmes:
                print(f"Título: {f.titulo} | Duração: {f.duracao}m | Gênero: {f.genero}")

        elif opcao == '3':
            print("\n--- Todas as Sessões ---")
            sessoes = controller.listar_sessoes()
            if not sessoes: print("Nenhuma sessão agendada.")
            for s in sessoes:
                print(f"Local: {s['cinema']} | Filme: {s['filme']} | Quando: {s['data_hora']}")

        elif opcao == '4':
            print("\n--- Sessões por Cinema ---")
            try:
                cid = int(input("Digite o ID do Cinema que deseja consultar: "))
                sessoes = controller.listar_sessoes(cinema_id=cid)
                if not sessoes: 
                    print("Nenhuma sessão encontrada para este cinema.")
                for s in sessoes:
                    print(f"Filme: {s['filme']} | Quando: {s['data_hora']}")
            except ValueError:
                print("\n=> ERRO: O ID do cinema deve ser um número!")

        elif opcao == '0':
            print("\nSaindo da área do público...")
            break
        else:
            print("\n=> Opção inválida! Tente novamente.")