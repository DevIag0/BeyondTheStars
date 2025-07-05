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

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def save_score(self, player_name, score):
        """Salva uma pontuação no banco de dados"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''
            INSERT INTO scores (player_name, score, date)
            VALUES (?, ?, ?)
        ''', (player_name, score, date_str))

        conn.commit()
        conn.close()

    def get_top_scores(self, limit=10):
        """Retorna as top pontuações limitadas pelo parâmetro limit"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT player_name, score, date
            FROM scores
            ORDER BY score DESC
            LIMIT ?
        ''', (limit,))

        scores = cursor.fetchall()
        conn.close()

        return scores

    def get_player_stats(self, player_name):
        """Retorna estatísticas de um jogador específico"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

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
