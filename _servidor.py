##{'number':'1', 'title':'Importando Bibliotecas', 'description'='Vamos utilizar basicamente a biblioteca asyncio para chamadas assincronas e websocket para comunicação'}
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
import sll
##{'number':'2', 'title':'Salvando os clientes', 'description'='Vamos guardar os clientes nesta lista. Isso permitirá enviar mensagens para quem estiver conectado.'}

CLIENTS = set()

async def echo(websocket):
    print("Nova conexão estabelecida")
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            print(f"Recebido: {message}")
            for client in CLIENTS:
                if client == websocket:
                    continue
                try:
                    print("Enviando...")
                    await client.send(message)
                except ConnectionClosed:
                    print("Erro ao enviar, conexão fechada...")
    finally:
        print("Conexão encerrada")
        CLIENTS.remove(websocket)

async def main():
    # Configurar o contexto SSL
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")  # Substitua pelo caminho do seu certificado e chave

    # Iniciar o servidor WebSocket com SSL
    server = await websockets.serve(echo, "localhost", 50000, ssl=ssl_context)
    print("Servidor iniciado com SSL na porta 50000")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
