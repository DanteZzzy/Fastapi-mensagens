import os
import json
import pika

def enviar_mensagem(msg):
    host = os.getenv("RABBITMQ_HOST", "localhost")
    fila = os.getenv("RABBITMQ_QUEUE", "mensagens")

    conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    canal = conexao.channel()

    canal.queue_declare(queue=fila, durable=True)
    canal.basic_publish(
        exchange="",
        routing_key=fila,
        body=json.dumps(msg),
        properties=pika.BasicProperties(delivery_mode=2),
    )

    print(f"[x] Mensagem enviada: {msg}")
    conexao.close()
