import sqlite3
from errors import DatabaseIntegrityError

class DBHandler:
    def __init__(self, db_name="dashboard.db"):
        self.db_name = db_name
        self._crear_tabla()

    def _crear_tabla(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    body TEXT
                )
            """)

    def guardar_posts(self, posts):
        try:
            with sqlite3.connect(self.db_name) as conn:
                for post in posts:
                    conn.execute(
                        "INSERT OR IGNORE INTO posts (id, title, body) VALUES (?, ?, ?)",
                        (post['id'], post['title'], post['body'])
                    )
        except Exception as e:
            raise DatabaseIntegrityError(f"Error al guardar en DB: {e}")

    def obtener_todos(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row # Esto nos permite leer por nombre de columna
            cursor = conn.execute("SELECT * FROM posts")
            return [dict(row) for row in cursor.fetchall()]