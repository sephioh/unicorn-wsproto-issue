import asyncio
import json
from collections import Counter

import uvicorn
from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute


def asgi_tasks():
    tasks = [task._coro.__name__ for task in asyncio.all_tasks()]
    task_counter = Counter(tasks)
    return json.dumps(task_counter)


class MainWebSocket(WebSocketEndpoint):
    encoding = "text"

    async def on_connect(self, websocket):
        await websocket.accept()

    async def on_receive(self, websocket, data):
        await websocket.send_text(asgi_tasks)

    async def on_disconnect(self, websocket, close_code):
        print(f"ON_DISCONNECT: close code: {close_code}")


routes = [WebSocketRoute("/ws", MainWebSocket)]

app = Starlette(routes=routes)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
