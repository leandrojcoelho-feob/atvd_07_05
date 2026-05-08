from services.service import CinemaService

class CinemaController:
    def __init__(self):
        self.service = CinemaService()

    def cadastrar_cinema(self, nome, capacidade, endereco):
        try:
            self.service.cadastrar_cinema(nome, int(capacidade), endereco)
            return True, "Cinema cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)

    def cadastrar_filme(self, titulo, duracao, diretor, genero):
        try:
            self.service.cadastrar_filme(titulo, int(duracao), diretor, genero)
            return True, "Filme cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)

    def criar_sessao(self, cinema_id, filme_id, data_hora):
        try:
            self.service.criar_sessao(int(cinema_id), int(filme_id), data_hora)
            return True, "Sessão criada com sucesso!"
        except Exception as e:
            return False, str(e)

    def registrar_publico(self, sessao_id, cinema_id, publico):
        try:
            self.service.registrar_publico(int(sessao_id), int(cinema_id), int(publico))
            return True, "Público registrado com sucesso!"
        except Exception as e:
            return False, str(e)

    # --- Consultas ---
    def listar_cinemas(self):
        return self.service.listar_cinemas()

    def listar_filmes(self):
        return self.service.listar_filmes()

    def listar_sessoes(self, cinema_id=None):
        return self.service.listar_sessoes_detalhadas(cinema_id)