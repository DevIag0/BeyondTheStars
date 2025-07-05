import sqlite3
import os
from datetime import datetime


class DatabaseProxy:
    def __init__(self, db_path="scores.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Inicializa o banco de dados e cria a tabela se não existir"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Primeiro, verifica se a tabela existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')

        # Verifica se a coluna game_mode existe, se não, adiciona ela
        cursor.execute("PRAGMA table_info(scores)")
        columns = [column[1] for column in cursor.fetchall()]

        if 'game_mode' not in columns:
            # Adiciona a coluna game_mode com valor padrão '60_seconds' para registros existentes
            cursor.execute('ALTER TABLE scores ADD COLUMN game_mode TEXT DEFAULT "60_seconds"')
            print("Coluna game_mode adicionada à tabela scores.")

        conn.commit()
        conn.close()

    def save_score(self, player_name, score, game_mode):
        """Salva uma pontuação no banco de dados com o modo de jogo"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''
            INSERT INTO scores (player_name, score, date, game_mode)
            VALUES (?, ?, ?, ?)
        ''', (player_name, score, date_str, game_mode))

        conn.commit()
        conn.close()

    def get_top_scores(self, limit=10, game_mode=None):
        """Retorna as top pontuações limitadas pelo parâmetro limit e filtradas por modo de jogo"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if game_mode:
            cursor.execute('''
                SELECT player_name, score, date
                FROM scores
                WHERE game_mode = ?
                ORDER BY score DESC
                LIMIT ?
            ''', (game_mode, limit))
        else:
            cursor.execute('''
                SELECT player_name, score, date
                FROM scores
                ORDER BY score DESC
                LIMIT ?
            ''', (limit,))

        scores = cursor.fetchall()
        conn.close()

        return scores

    def get_player_stats(self, player_name, game_mode=None):
        """Retorna estatísticas de um jogador específico, opcionalmente filtradas por modo"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if game_mode:
            # Total de jogos no modo específico
            cursor.execute('''
                SELECT COUNT(*) FROM scores WHERE player_name = ? AND game_mode = ?
            ''', (player_name, game_mode))
            total_games = cursor.fetchone()[0]

            # Melhor pontuação no modo específico
            cursor.execute('''
                SELECT MAX(score) FROM scores WHERE player_name = ? AND game_mode = ?
            ''', (player_name, game_mode))
            best_score = cursor.fetchone()[0] or 0
        else:
            # Total de jogos
            cursor.execute('''
                SELECT COUNT(*) FROM scores WHERE player_name = ?
            ''', (player_name,))
            total_games = cursor.fetchone()[0]

            # Melhor pontuação
            cursor.execute('''
                SELECT MAX(score) FROM scores WHERE player_name = ?
            ''', (player_name,))
            best_score = cursor.fetchone()[0] or 0

        conn.close()

        return {
            'total_games': total_games,
            'best_score': best_score
        }

    def get_all_players(self):
        """Retorna lista de todos os jogadores únicos"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT DISTINCT player_name FROM scores
            ORDER BY player_name
        ''')

        players = [row[0] for row in cursor.fetchall()]
        conn.close()

        return players
