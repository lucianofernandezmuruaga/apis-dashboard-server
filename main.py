from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database_handler import DBHandler
from api_handler import APIHandler
from errors import APIConnectionError

app = FastAPI()
db = DBHandler()
api = APIHandler("https://jsonplaceholder.typicode.com/posts")

# Dónde están las plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse("reporte.html", {"request": request, "data": db.obtener_todos()})

@app.get("/actualizar")
def actualizar_datos():
    # Comienza el bot
    try:
        datos = api.obtener_datos()
        db.guardar_posts(datos)
        return RedirectResponse(url="/?msg=Actualizacion+Exitosa", status_code=303)

    except APIConnectionError as e:
        return RedirectResponse(url=f"/?error={str(e)}", status_code=303)


@app.get("/reporte")
def ver_reporte():
    # La API nos devuelve lo que hay en la base de datos
    datos_locales = db.obtener_todos()
    return {"data": datos_locales}

#uvicorn main:app --reload