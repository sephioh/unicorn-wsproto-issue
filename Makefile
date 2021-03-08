PORT=8080
HOST=0.0.0.0


websockets:
	pipenv shell uvicorn main:app --reload --host $(HOST) --ws websockets --port $(PORT)

wsproto:
	pipenv shell uvicorn main:app --reload --host $(HOST) --ws wsproto --port $(PORT)
