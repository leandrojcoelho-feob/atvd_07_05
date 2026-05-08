import sqlite3
from models.models import Cinema, Filme, Sessao

class DatabaseSetup:
    @staticmethod
    def initialize():
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cinemas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT, capacidade INTEGER, endereco TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT, duracao INTEGER, diretor TEXT, genero TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cinema_id INTEGER, filme_id INTEGER,
                data_hora TEXT, publico INTEGER,
                FOREIGN KEY(cinema_id) REFERENCES cinemas(id),
                FOREIGN KEY(filme_id) REFERENCES filmes(id)
            )
        ''')
        conn.commit()
        conn.close()

class CinemaRepository:
    def salvar(self, nome, capacidade, endereco):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO cinemas (nome, capacidade, endereco) VALUES (?, ?, ?)', 
                       (nome, capacidade, endereco))
        conn.commit()
        conn.close()

    def buscar_por_id(self, cinema_id):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cinemas WHERE id = ?', (cinema_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Cinema(id=row[0], nome=row[1], capacidade=row[2], endereco=row[3])
        return None

    def buscar_todos(self):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cinemas')
        rows = cursor.fetchall()
        conn.close()
        return [Cinema(id=r[0], nome=r[1], capacidade=r[2], endereco=r[3]) for r in rows]

class FilmeRepository:
    def salvar(self, titulo, duracao, diretor, genero):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO filmes (titulo, duracao, diretor, genero) VALUES (?, ?, ?, ?)', 
                       (titulo, duracao, diretor, genero))
        conn.commit()
        conn.close()

    def buscar_por_id(self, filme_id):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM filmes WHERE id = ?', (filme_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Filme(id=row[0], titulo=row[1], duracao=row[2], diretor=row[3], genero=row[4])
        return None

    def buscar_todos(self):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM filmes')
        rows = cursor.fetchall()
        conn.close()
        return [Filme(id=r[0], titulo=r[1], duracao=r[2], diretor=r[3], genero=r[4]) for r in rows]

class SessaoRepository:
    def salvar(self, cinema_id, filme_id, data_hora):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO sessoes (cinema_id, filme_id, data_hora, publico) VALUES (?, ?, ?, 0)',
                       (cinema_id, filme_id, data_hora))
        conn.commit()
        conn.close()

    def registrar_publico(self, sessao_id, publico):
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE sessoes SET publico = ? WHERE id = ?', (publico, sessao_id))
        conn.commit()
        conn.close()

    def buscar_todas_com_detalhes(self, cinema_id=None):
        """Busca sessões cruzando dados com filmes e cinemas. Opcionalmente filtra por cinema."""
        conn = sqlite3.connect('cinema.db')
        cursor = conn.cursor()
        
        query = '''
            SELECT s.id, c.nome, f.titulo, s.data_hora, s.publico 
            FROM sessoes s
            JOIN cinemas c ON s.cinema_id = c.id
            JOIN filmes f ON s.filme_id = f.id
        '''
        
        if cinema_id:
            query += ' WHERE s.cinema_id = ?'
            cursor.execute(query, (cinema_id,))
        else:
            cursor.execute(query)
            
        rows = cursor.fetchall()
        conn.close()
        
        # Retornamos dicionários para facilitar a exibição na View
        return [{"sessao_id": r[0], "cinema": r[1], "filme": r[2], "data_hora": r[3], "publico": r[4]} for r in rows]