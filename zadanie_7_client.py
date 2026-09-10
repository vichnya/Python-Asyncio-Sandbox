#python zadanie_7_client.py

import asyncio
import json

async def send_message():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8080)

    while True:
        message = input("Введите сообщение ('exit' для разрыва соединения): ")
        writer.write(message.encode('utf-8'))
        await writer.drain()

        if message.lower() == 'exit':
            break

        data = await reader.read(100)
        response = json.loads(data.decode('utf-8'))
        print(f"Отправленное сообщение: {response['message']}")

    print("Окончание соединения")
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    try:
        asyncio.run(send_message())
    except KeyboardInterrupt:
        pass
