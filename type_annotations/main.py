# type annotations 

def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print(greet("Alice"))
    print(add(5.1, 3.0)) # Esto no falla en tiempo de ejecución, pero mypy o pyright lo marcarían como error.
    
#🧠 Si este código no falla, entonces… ¿para qué sirven las anotaciones?
    # Sirven para:
    # Herramientas de análisis estático como mypy, pyright, o los chequeos de tipo de VS Code.
    # Mejor autocompletado y documentación en IDEs.
    # Evitar errores antes de ejecutar el código.

from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# Prueba con:
# GET /add?a=5&b=3
{"result": 8}

# Pero si pruebas con:
# GET /add?a=5.1&b=3.0

{
  "detail": [
    {
      "loc": ["query", "a"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}

# ⚙️ ¿Por qué aquí sí falla?
# Porque FastAPI usa Pydantic (y en las versiones más recientes, Pydantic v2) para:
# Validar los tipos de entrada (query params, body, path params…).
# Convertir datos automáticamente (por ejemplo, strings a int o float).
# Generar errores si el tipo no coincide.
# En otras palabras:
# En FastAPI, los tipos se imponen y validan automáticamente en los endpoints, no solo se anotan.
