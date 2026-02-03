import unittest
import os
from database_handler import DBHandler


class TestDBHandler(unittest.TestCase):
    def setUp(self):
        # Base de 'test'
        self.test_db = "test_temp.db"
        self.db = DBHandler(self.test_db)

    def tearDown(self):
        if hasattr(self, 'db'):
            del self.db

        # Se borra la base de test
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except PermissionError:
                print("Windows todavía no soltó el archivo, pero el test ya pasó.")

    def test_guardar_y_obtener_posts(self):
        datos_prueba = [
            {"id": 999, "title": "Test Title", "body": "Test Body"}
        ]

        self.db.guardar_posts(datos_prueba)
        resultados = self.db.obtener_todos()

        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]['title'], "Test Title")


if __name__ == "__main__":
    unittest.main()