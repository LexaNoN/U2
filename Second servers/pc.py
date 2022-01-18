from fastapi import FastAPI, HTTPException, Request
import uvicorn
from random import randint
from os import path, system
import requests
from win10toast import ToastNotifier

toaster = ToastNotifier()
app = FastAPI()

commands = [
    ["/", "get", "name of pc"],
    ["/shutdown", "get", "shutdown"],
    ["/notify/{name}/{text}", "post", "send notify"]
]

@app.get("/")
def read_root():
    return {"name": "PC"}

@app.get("/ping")
def read_root():
    return {"pong": "PC"}

@app.get("/shutdown")
def read_root():
    system("shutdown /s /t 1")

# http://127.0.0.1:8000/name/text.
@app.post("/notify/{name}/{text}")
def read_item(name: str, text: str):
    toaster.show_toast(name,
                       text,
                       icon_path=None,
                       duration=5,
                       threaded=True)
    return {"status": "OK"}

_name = path.basename(__file__)
if __name__ == "__main__":
    port = randint(5001, 5999)
    print(port)
    name = "PC-Lexanon"
    try:
        requests.post('http://127.0.0.1:5000/server/add_client/%s/%s/%s' % (name, str(port), commands))
    except requests.exceptions.ConnectionError:
        print("Cannot connect to server! \n" * 3)
    uvicorn.run(str(_name[:len(_name) - 3]) + ":app", host="localhost", port=port, log_level="info")
