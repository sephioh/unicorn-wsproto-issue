import asyncio
import sys

import websocket

CONNECTIONS = 10


def get_ongoing_tasks():
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8080/ws")
    ws.send("")
    result = ws.recv()
    print(result)
    ws.close()


async def multiple_bad_connections():
    """Create multiple connections but do not close them properly."""
    async def connect():
        ws = websocket.WebSocket()
        ws.connect("ws://localhost:8080/ws")

    tasks = [asyncio.create_task(connect()) for i in range(CONNECTIONS)]
    await asyncio.gather(*tasks)

    print(f"{CONNECTIONS} connections created but not properly closed.")


if __name__ == "__main__":
    argv = sys.argv
    assert len(argv) == 2
    mode = argv[1]

    if mode == "batch":
        el = asyncio.get_event_loop()
        el.run_until_complete(multiple_bad_connections())
    else:
        get_ongoing_tasks()
