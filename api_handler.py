import requests
from errors import APIConnectionError


class APIHandler:
    def __init__(self, url):
        self.url = url

    def obtener_datos(self):
        try:
            respuesta = requests.get(self.url, timeout=5)
            # Si el status no es 200, lanzamos nuestra propia alarma
            if respuesta.status_code != 200:
                raise APIConnectionError(f"La API respondió con error: {respuesta.status_code}")

            return respuesta.json()

        except requests.exceptions.RequestException as e:
            # Capturamos el error técnico y lo transformamos en nuestro error personalizado
            raise APIConnectionError(f"Fallo total de conexión: {str(e)}")