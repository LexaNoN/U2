import json
import requests

response = requests.get("http://127.0.0.1:5000/openapi.json")
todos = json.loads(response.text)
todos = todos["paths"]
for comm in todos:
    method = None
    for meth in todos[comm]:
        method = meth
    summary = todos[comm][method]["summary"]
    try:
        desc = todos[comm][method]["description"]
    except KeyError:
        continue
    print(comm, method, summary, desc)