from fastapi import FastAPI

app = FastAPI(title="Primos Pobres")


@app.get("/health")
def health():
    return {"status": "ok"}
