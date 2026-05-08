from dataclasses import dataclass

@dataclass
class Cinema:
    id: int
    nome: str
    capacidade: int
    endereco: str

@dataclass
class Filme:
    id: int
    titulo: str
    duracao: int
    diretor: str
    genero: str

@dataclass
class Sessao:
    id: int
    cinema_id: int
    filme_id: int
    data_hora: str
    publico: int