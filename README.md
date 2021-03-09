# uvicorn-wsproto-issue
This project tries to display the problem with wsproto implementation on
uvicorn.
Differently than websockets impl, wsproto impl leaves zombie tasks ongoing after clients
forget to properly close connections.

## Running
Make sure you have pipenv installed.

### wsproto
```bash
# Start the app running wsproto impl with:
make wsproto

# Leave the app running and simulate 10 bad connections with:
make batch-connections

# Check ongoing tasks sending a message to websocket endpoint:
make check-tasks

# Verify that the number of run_asgi tasks is 11 (it should be 1).
# {"run_asgi": 11, "main": 1, "serve": 1}
```

### websockets
```bash
# Close other running instances to avoid port conflicts (both use the same port).

# Start the app running websockets impl with:
make websockets

# Leave the app running and simulate 10 bad connections with:
make batch-connections

# Check ongoing tasks sending a message to websocket endpoint:
make check-tasks

# Verify that the number of run_asgi tasks is 1 (as expected).
# {"keepalive_ping": 1, "close_connection": 1, "transfer_data": 1, "run_asgi": 1, "handler": 1, "main": 1, "serve": 1}
```
