from repository.repository import DatabaseSetup
from view.view_func import menu_funcionario
from view.view_publico import menu_publico

def iniciar_app():
    # Inicializa o banco de dados
    DatabaseSetup.initialize()
    
    while True:
        print("\n" + "="*45)
        print("--- BEM-VINDO AO SISTEMA DE CINEMAS ---")
        print("="*45)
        print("Selecione o seu perfil de acesso:")
        print("[1] Funcionário")
        print("[2] Público")
        print("[0] Sair do Aplicativo")
        print("="*45)
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            matricula = input("Digite sua matrícula de funcionário: ")
            
            # Validação simples: se digitou qualquer coisa, entra. 
            # Em um sistema real, consultaríamos a matrícula no banco de dados.
            if matricula.strip():
                print(f"\nAcesso concedido. Bem-vindo(a), funcionário #{matricula}!")
                menu_funcionario()
            else:
                print("\n=> ERRO: Matrícula inválida! Acesso negado.")
                
        elif opcao == '2':
            menu_publico()
            
        elif opcao == '0':
            print("\nEncerrando o sistema... Até logo e bom filme!")
            break
            
        else:
            print("\n=> Opção inválida! Tente novamente.")

if __name__ == "__main__":
    iniciar_app()