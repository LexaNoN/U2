from fastapi import FastAPI, Request
from multiprocessing import Process
from random import randint
from time import sleep
from os import path
import requests
import logging
import uvicorn

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/",
          summary="Hello World",
          description="Get Hello World")
def read_root():
    return {"Hello": "World"}


# http://127.0.0.1:8000/items/5?q=somequery.
@app.post("/client/print/{text}",
          summary="Print",
          description="Print something in console")
def read_item(text: str):
    print(text)
    return {"status": "OK"}


def connMainframe(_name, _port):
    sleep(5)
    try:
        print("321")
        requests.post('http://127.0.0.1:5000/server/add_client/%s/%s' % (_name, str(_port)))
        logger.info("Connect successfully")
    except requests.exceptions.ConnectionError:
        exit("Cannot connect to server!")


def startUvicorn(_port):
    uvicorn.run(str(_name[:len(_name) - 3]) + ":app", host="localhost", port=_port, log_level="error")


_name = path.basename(__file__)
if __name__ == "__main__":
    name = "simp"
    port = randint(5020, 5999)
    print(port)
    p1 = Process(target=connMainframe, args=(name, port))
    p1.start()
    print("1212")
    p2 = Process(target=startUvicorn, args=(port,))
    p2.start()
