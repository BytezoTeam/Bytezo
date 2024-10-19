import niquests


def send_push(key: str, name: str, id: str):
    pushsaver_url = "https://www.pushsafer.com/api"
    server_url = "localhost:8000"

    parameters = {
        "t": "New Bytezo Message",
        "m": f"{name} send a message for Bytezo",
        "s": 11,
        "v": 3,
        "i": 33,
        "c": "#FF0000",
        "d": "a",
        "u": f"http://{server_url}/get_message/{id}",
        "ut": "Open Full Message",
        "k": key,
    }

    request = niquests.post(pushsaver_url, params=parameters)
    print(request.text)
