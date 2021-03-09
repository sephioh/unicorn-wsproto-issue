import asyncio
from collections import Counter

import uvicorn


def asgi_tasks():
    tasks = [task._coro.__name__ for task in asyncio.all_tasks()]
    task_counter = Counter(tasks)
    return str(dict(task_counter))


async def app(scope, receive, send):
    assert scope["type"] == "websocket"

    await send(
        {
            "type": "websocket.accept",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )

    while True:
        message = await receive()
        if message["type"] == "websocket.receive":
            await send({"type": "websocket.send", "text": asgi_tasks()})

        if message["type"] == "websocket.disconnect":
            break


if __name__ == "__main__":
    uvicorn.run(app=app)
