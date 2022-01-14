from typing import Optional, List
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pythonping import ping
from os import system, path
import uvicorn
import requests
import logging
import serviceping
from pydantic import BaseModel

# TODO Make normal JSON transmit
# https://python-scripts.com/json#decoding-custom-types

app = FastAPI()
clients = []
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/dummypath",
          summary="Create an item", # TODO ADD TO ALL
          description="Create an item with all the information, name, description, price, tax and a set of unique tags",
          )
async def get_body(request: Request):
    return await request.body()

# http://127.0.0.1:8000/items/5?q=somequery.

@app.get("/server/getinfo")
def read_item():
    return {"count client": len(clients), "clients": clients}


def send_to_service(_ip, name, prog, param):
    id = None
    for l in range(len(clients)):  # Find ID of client
        try:
            id = clients[l].index(name)
        except ValueError:
            pass
    if id is not None:  # If we get something
        _ping = serviceping.scan(str(clients[id][1]), port=str(clients[id][2])).get("state")  # Ping
        if _ping == "closed":
            logger.warning(("Client closed!", _ip, name, prog, param))
            clients.pop(id)
            return HTTPException(status_code=504, detail="Client is lost (maybe crashed)!")
        requests.post('http://127.0.0.1:%s/client/%s/%s/' % (clients[id][2], prog, param))
        logger.info(("Request", _ip, name, prog, param))
    else:
        logger.warning(("Client not founded!", _ip, name, prog, param))
        return HTTPException(status_code=404, detail="Client is not exciting!")


# http://127.0.0.1:8000/items/5?q=somequery.
@app.post("/server/add_client/{name}/{port}/{comm}")
def read_item(name: str, port: int, comm, request: Request):
    id = None
    ip = request.client.host
    for i in range(len(comm)):
        print(comm[i][0])
        comm[i][0] = str(comm[i][0]).replace("|", "/")  # TODO тестить вот это
    for l in range(len(clients)):
        try:
            id = clients[l].index(name)
        except ValueError:
            pass
    if id is not None:
        clients.pop(id)
        logger.info(("ReConnected", name, ip, port))
        logger.debug(comm)
    else:
        clients.append([name, ip, port, comm])
        logger.info(("Connected", name, ip, port))
        logger.debug(comm)
    if name[:2] == "PC":
        pc_name = name[3:]
        send_to_service("Iternal", "TG_log", "ON", pc_name)
        logger.debug(("TG_log ", "ON", pc_name))
    return {"status": "OK"}

@app.post("/server/send/{name}/{prog}/{param}")
def read_item(name: str, prog: str, param: str, request: Request):
    ip = str(request.client.host) + ":" + str(request.client.port)
    return send_to_service(ip, name, prog, param)  # Check is raise and return is similar in 404


_name = path.basename(__file__)
if __name__ == "__main__":
    ip = "localhost" # If uvicorn get loop'd in module "selector" (watch debug), change ip to smth else
    port = 5000
    logger.info("Starting host on http://%s:%s" % (ip, port))
    uvicorn.run(str(_name[:len(_name) - 3]) + ":app", host=ip, port=port, log_level="error")
    logger.info("Ready!")
