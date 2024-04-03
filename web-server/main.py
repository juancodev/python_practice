import api_store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# creamos una instancia de la clase FastAPI
app = FastAPI()

# agregamos los decoradores
@app.get('/')
def get_list():
  return [1,2,3,4]

#renderizando HTML
@app.get('/contact', response_class=HTMLResponse)
def get_list():
  return '''
    <h1>Hola, soy un titulo</h1>
    <p>Soy un parrafo desde el renderizado del server</p>
  '''
def run():
  api_store.get_products()

if __name__ == "__main__":
  run()

