# API Dashboard Server 🚀

Este proyecto es un servidor web completo desarrollado en Python que automatiza la recolección de datos desde APIs externas, los almacena en una base de datos local y los visualiza a través de un panel de control dinámico.

## 🛠️ Tecnologías Utilizadas
- **Backend**: FastAPI & Uvicorn (Servidor ASGI).
- **Base de Datos**: SQLite3 con persistencia de datos.
- **Frontend**: Plantillas Jinja2 con HTML5 y CSS3.
- **Testing**: Librería `unittest` para validación de lógica de negocio y manejo de excepciones.

## 📂 Características Principales
- **Manejo de Errores Avanzado**: Implementación de excepciones personalizadas para gestionar fallos de red o de base de datos de forma elegante.
- **Dashboard Visual**: Interfaz web para visualizar los registros almacenados en tiempo real.
- **Documentación Interactiva**: Gracias a FastAPI, el proyecto incluye documentación automática en la ruta `/docs`.
- **Testing Automático**: Scripts de prueba para asegurar que el sistema maneje correctamente los errores de conexión.

## ⚙️ Instalación y Uso

1. **Clonar el repositorio** y situarse en la carpeta del proyecto.
2. **Instalar dependencias**:
   ```bash
   pip install fastapi uvicorn requests jinja2
   ```
3. **Ejecutar el servidor**:
   ```bash
   uvicorn main:app --reload
   ```
4. **Navegar**:
   - Inicio/Reporte: `http://127.0.0.1:8000/`
   - Forzar actualización: `http://127.0.0.1:8000/actualizar`
   - Documentación: `http://127.0.0.1:8000/docs`

## 🧪 Ejecución de Pruebas
Para verificar el correcto funcionamiento del manejo de errores:
```bash
python test_api.py
```