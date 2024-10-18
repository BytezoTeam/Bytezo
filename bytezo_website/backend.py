from urllib.parse import urlencode
from urllib.request import Request, urlopen


def send_push(key: str, name: str, id: str):
    url = 'https://www.pushsafer.com/api'
    post_fields = {
        "t" : f'New Bytezo Message',
        "m" : f"{name} send a message for Bytezo",
        "s" : 11,
        "v" : 3,
        "i" : 33,
        "c" : '#FF0000',
        "d" : 'a',
        "u" : f'http://192.168.178.80:8000/get_message/{id}',
        "ut" : 'Open Full Message',
        "k" : key,
        }

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)