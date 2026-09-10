#python zadanie_7_server.py

import asyncio
import json

async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode('utf-8')
        if message.lower() == 'exit':
            break
        print(f"Сообщение: {message}")

        response = {'message': message}
        writer.write(json.dumps(response).encode('utf-8'))
        await writer.drain()

    print("Окончание соединения")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8080
    )

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
