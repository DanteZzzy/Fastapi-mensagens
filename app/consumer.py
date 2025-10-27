import os
import json
import pika

def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print(f"[✔] Mensagem recebida: {mensagem}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consumir():
    host = os.getenv("RABBITMQ_HOST", "localhost")
    fila = os.getenv("RABBITMQ_QUEUE", "mensagens")

    conexao = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    canal = conexao.channel()

    canal.queue_declare(queue=fila, durable=True)
    canal.basic_qos(prefetch_count=1)
    canal.basic_consume(queue=fila, on_message_callback=callback)

    print("🟢 Aguardando mensagens. Pressione CTRL+C para sair.")
    canal.start_consuming()

if __name__ == "__main__":
    consumir()
