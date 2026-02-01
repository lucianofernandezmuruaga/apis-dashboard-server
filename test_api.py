import unittest
from api_handler import APIHandler
from errors import APIConnectionError


class TestAPI(unittest.TestCase):
    def test_url_invalida_lanza_error(self):
        # Probamos que una URL que no existe realmente lance nuestro error
        handler = APIHandler("https://url-que-no-existe-123.com")

        with self.assertRaises(APIConnectionError):
            handler.obtener_datos()


if __name__ == "__main__":
    unittest.main()