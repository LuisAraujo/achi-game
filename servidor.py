##{"number":"1", "title":"Importando Bibliotecas", "description":"Vamos utilizar basicamente a biblioteca asyncio para chamadas assincronas e websocket para comunicação"}

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

##{"number":"2", "title":"Salvando os clientes", "description":"Vamos guardar os clientes nesta lista. Isso permitirá enviar mensagens para quem estiver conectado."}

CLIENTS = set()

##{"number":"3", "title":"Função handle", "description":"Esta função será chamada a cada conexão realizada e envio de mensagens."}
async def handle(websocket):

    #primeiro adicionaremos na lista de clientes
    CLIENTS.add(websocket)
    #para cada mensagem recebida
    async for message in websocket:
        #enciando para todos os clientes com exceção de quem enviou
        for client in CLIENTS:
            if(client == websocket):
                continue;
            try:
                print("enviando...")
                await client.send(message)
            except ConnectionClosed:
                print("erro ao enviar...")
                pass
##{"number":"4", "title":"Serve", "description":"Subindo o servidor em localhost na porta 50000."}

start_server = websockets.serve(handle, "localhost", 50000)
#cadastrando eventos
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
