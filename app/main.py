from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from producer import enviar_mensagem

app = FastAPI(title="FastAPI + RabbitMQ")

class Mensagem(BaseModel):
    nome: str
    texto: str

@app.post("/enviar")
def enviar(msg: Mensagem):
    try:
        enviar_mensagem(msg.dict())
        return {"status": "enviado", "mensagem": msg}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
