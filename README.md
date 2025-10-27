```markdown
# 📬 FastAPI + RabbitMQ com Docker Compose

Este projeto demonstra a integração entre **FastAPI** (aplicação principal) e **RabbitMQ** (sistema de mensageria) utilizando **Docker Compose**.  
O objetivo é criar uma API REST que envie mensagens para uma fila RabbitMQ e um consumidor que lê e exibe essas mensagens no terminal.

---

## 🧱 Estrutura do Projeto

```

P2-T1/
│
├── app/
│   ├── main.py          # Aplicação FastAPI (produtor)
│   ├── consumer.py      # Consumidor RabbitMQ
|   ├── producer.py      # Produtor(envia mensagens para RabbitMQ)
│   ├── Dockerfile       # Configuração da imagem FastAPI
│   └── requirements.txt # Dependências Python
│
├── docker-compose.yml     # Configuração dos containers (FastAPI + RabbitMQ)
└── README.md              # Documentação do projeto

````

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **pika** (cliente RabbitMQ)
- **RabbitMQ 3-management**
- **Docker & Docker Compose**

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/p2-t1-fastapi-rabbitmq.git
cd p2-t1-fastapi-rabbitmq
````

### 2️⃣ Subir os containers com Docker Compose

```bash
docker compose up --build
```

Isso iniciará:

* O servidor **FastAPI** na porta **8000**
* O **RabbitMQ** com painel de gerenciamento na porta **15672**

---

## 🌐 Acessos

| Serviço              | URL                                                      |
| -------------------- | -------------------------------------------------------- |
| FastAPI (Swagger UI) | [http://localhost:8000/docs](http://localhost:8000/docs) |
| RabbitMQ Management  | [http://localhost:15672/](http://localhost:15672/)       |

Credenciais padrão do RabbitMQ:

* **Usuário:** guest
* **Senha:** guest

---

## 📡 Envio de Mensagem

Você pode enviar uma mensagem de três formas:

### ✅ Via Swagger

Acesse [http://localhost:8000/docs](http://localhost:8000/docs), selecione `POST /enviar`, clique em **Try it out** e insira:

```json
{
  "nome": "Gabriel",
  "texto": "Mensagem de teste com RabbitMQ"
}
```

### ✅ Via terminal (PowerShell)

```powershell
Invoke-WebRequest -Uri "http://localhost:8000/enviar" -Method POST -Body '{"nome": "Gabriel", "texto": "Mensagem de teste com RabbitMQ"}' -Headers @{"Content-Type"="application/json"}
```

### ✅ Via terminal (cmd ou Git Bash)

```bash
curl.exe -X POST http://localhost:8000/enviar -H "Content-Type: application/json" -d "{\"nome\":\"Gabriel\", \"texto\":\"Mensagem de teste com RabbitMQ\"}"
```

---

## 🧾 Funcionamento

### 🔸 Endpoint `/enviar`

* Recebe um JSON contendo `nome` e `texto`.
* Envia a mensagem para a fila **mensagens** no RabbitMQ.

### 🔸 Consumidor (`consumer.py`)

* Lê continuamente as mensagens da fila.
* Exibe no terminal o conteúdo recebido.

Para rodar o consumidor manualmente (caso não esteja automático no `docker-compose`):

```bash
docker exec -it fastapi_app python app/consumer.py
```

Saída esperada:

```
🟢 Aguardando mensagens. Pressione CTRL+C para sair.
[✔] Mensagem recebida: {'nome': 'Gabriel', 'texto': 'Mensagem de teste com RabbitMQ'}
```

---

## 🧰 Comandos Úteis

Parar containers:

```bash
docker compose down
```

Rebuildar completamente:

```bash
docker compose up --build
```

Ver containers ativos:

```bash
docker ps
```

---

## 🧑‍💻 Autor

| Nome                          | Função                                        |
| ----------------------------- | --------------------------------------------- |
| **Gabriel Teixeira de Faria** | Desenvolvimento e Integração FastAPI-RabbitMQ |

---

## 📜 Licença

Este projeto é de uso acadêmico, desenvolvido para a disciplina de **Banco de Dados Não Relacional** — Universidade Vassouras, Campus Maricá.

---

> 💡 **Resumo:**
>
> * `FastAPI` → recebe e envia mensagens
> * `RabbitMQ` → gerencia a fila
> * `consumer.py` → lê e imprime mensagens recebidas

```

-
