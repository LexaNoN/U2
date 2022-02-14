import requests
print("Клиент для запроса внутри сети U2")
ip = "127.0.0.1"
port = "5000"
name = input(": ")
is_get = True
method = input(": ")
argument = input(": ")
if is_get is True:
    r = requests.post("http://" + ip + ":"
                 + port + "/server/send/%s/%s/%s"
                 % (name, method, argument))
    if r.status_code == 200:
        print("OK")
    else:
        print(r.status_code, r.text)