import sqlite3


class BancoDeDados:
    def __init__(self, nome_do_arquivo='dados.db'):
        self.nome_do_arquivo = nome_do_arquivo

    def criar_tabelas(self):
        conexao = sqlite3.connect(self.nome_do_arquivo)
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                            id INTEGER PRIMARY KEY,
                            nome TEXT,
                            idade INTEGER,
                            email TEXT,
                            cpf TEXT
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS evento (
                            id INTEGER PRIMARY KEY,
                            nome_evento TEXT,
                            endereco TEXT,
                            categoria TEXT,
                            horario TEXT,
                            descricao TEXT
                        )''')

        conexao.commit()
        conexao.close()

    def inserir_usuario(self, nome, idade, email, cpf):
        conexao = sqlite3.connect(self.nome_do_arquivo)
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO usuario (nome, idade, email, cpf) VALUES (?, ?, ?, ?)''',
                       (nome, idade, email, cpf))

        conexao.commit()
        conexao.close()

    def inserir_evento(self, nome_evento, endereco, categoria, horario, descricao):
        conexao = sqlite3.connect(self.nome_do_arquivo)
        cursor = conexao.cursor()

        cursor.execute(
            '''INSERT INTO evento (nome_evento, endereco, categoria, horario, descricao) VALUES (?, ?, ?, ?, ?)''',
            (nome_evento, endereco, categoria, horario, descricao))

        conexao.commit()
        conexao.close()

    def listar_usuarios(self):
        conexao = sqlite3.connect(self.nome_do_arquivo)
        cursor = conexao.cursor()

        cursor.execute('''SELECT * FROM usuario''')
        usuarios = cursor.fetchall()

        conexao.close()
        return usuarios

    def listar_eventos(self):
        conexao = sqlite3.connect(self.nome_do_arquivo)
        cursor = conexao.cursor()

        cursor.execute('''SELECT * FROM evento''')
        eventos = cursor.fetchall()

        conexao.close()
        return eventos

    # Adicione outras operações conforme necessário


# Exemplo de uso da classe BancoDeDados
banco = BancoDeDados()

# Cria as tabelas no banco de dados
banco.criar_tabelas()

# Insere um novo usuário e um novo evento
banco.inserir_usuario('Maria', 30, 'maria@email.com', '123456789')
banco.inserir_evento('Festa de Ano Novo', 'Rua Principal, 123', 'Celebration', '31/12/2023 22:00',
                     'Venha comemorar o Ano Novo conosco!')

# Lista todos os usuários e eventos
usuarios = banco.listar_usuarios()
eventos = banco.listar_eventos()

# Imprime os resultados
print("Usuários:")
for usuario in usuarios:
    print(usuario)

print("\nEventos:")
for evento in eventos:
    print(evento)

import sqlite3