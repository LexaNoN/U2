from fastapi import FastAPI, HTTPException, Request
import uvicorn
from random import randint
from os import path
import requests

app = FastAPI()

# there, we replace / with |, because http read / like test.com/test/command1 >|<, command2
commands = {
    ["|", "get", "name of pc"],
    ["|shutdown", "get", "shutdown"],
    ["|notify|{name}|{text}", "post", "send notify"]
}



@app.get("/")
def read_root():
    return {"Hello": "World"}


# http://127.0.0.1:8000/items/5?q=somequery.
@app.post("/server/add_client/{name}/{port}")
def read_item(name: str, port: int, request: Request):
    ip = request.client.host
    return {"status": "OK"}


# http://127.0.0.1:8000/items/5?q=somequery.
@app.post("/client/print/{text}")
def read_item(text: str):
    print(text)
    return {"status": "OK"}


_name = path.basename(__file__)
if __name__ == "__main__":
    port = randint(5001, 5999)
    print(port)
    name = "simp"
    try:
        requests.post('http://127.0.0.1:5000/server/add_client/%s/%s/%s' % (name, str(port), commands))
    except requests.exceptions.ConnectionError:
        exit("Cannot connect to server!")
    uvicorn.run(str(_name[:len(_name) - 3]) + ":app", host="localhost", port=port, log_level="info")