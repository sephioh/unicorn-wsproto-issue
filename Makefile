.PHONY: websockets wsproto batch-connections check-tasks
HOST=localhost
PORT=8080


websockets:
	pipenv run uvicorn main:app --reload --ws websockets --host $(HOST) --port $(PORT)

wsproto:
	pipenv run uvicorn main:app --reload --ws wsproto --host $(HOST) --port $(PORT)

batch-connections:
	pipenv run python client.py batch

check-tasks:
	pipenv run python client.py get-ongoing-tasks
