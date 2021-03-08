# unicorn-wsproto-issue
This project tries to display the problem with wsproto implementation on
uvicorn.
Differently than websockets impl, wsproto impl leaves zombie tasks ongoing after clients
forget to close connections.

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
```

### websockets
```bash
# Start the app running websockets impl with:
make websockets


# Leave the app running and simulate 10 bad connections with:
make batch-connections


# Check ongoing tasks sending a message to websocket endpoint:
make check-tasks


# Verify that the number of run_asgi tasks is 1 (as expected).
```
