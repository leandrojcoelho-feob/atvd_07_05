from repository.repository import CinemaRepository, SessaoRepository, FilmeRepository

class CinemaService:
    def __init__(self):
        self.cinema_repo = CinemaRepository()
        self.sessao_repo = SessaoRepository()
        self.filme_repo = FilmeRepository() # Novo repositório

    def cadastrar_cinema(self, nome, capacidade, endereco):
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        self.cinema_repo.salvar(nome, capacidade, endereco)

    def cadastrar_filme(self, titulo, duracao, diretor, genero):
        if duracao <= 0:
            raise ValueError("A duração deve ser maior que zero minutos.")
        self.filme_repo.salvar(titulo, duracao, diretor, genero)

    def criar_sessao(self, cinema_id, filme_id, data_hora):
        if not self.cinema_repo.buscar_por_id(cinema_id):
            raise ValueError("Cinema não encontrado.")
        if not self.filme_repo.buscar_por_id(filme_id):
            raise ValueError("Filme não encontrado.")
            
        self.sessao_repo.salvar(cinema_id, filme_id, data_hora)

    def registrar_publico(self, sessao_id, cinema_id, publico):
        cinema = self.cinema_repo.buscar_por_id(cinema_id)
        if not cinema:
            raise ValueError("Cinema não encontrado.")
        if publico > cinema.capacidade:
            raise ValueError(f"Público ({publico}) excede a capacidade do cinema ({cinema.capacidade}).")
        
        self.sessao_repo.registrar_publico(sessao_id, publico)

    # --- Novos Métodos de Consulta ---
    def listar_cinemas(self):
        return self.cinema_repo.buscar_todos()

    def listar_filmes(self):
        return self.filme_repo.buscar_todos()

    def listar_sessoes_detalhadas(self, cinema_id=None):
        return self.sessao_repo.buscar_todas_com_detalhes(cinema_id)