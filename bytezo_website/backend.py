from urllib.parse import urlencode
from urllib.request import Request, urlopen


def send_push(key, message, name):
    url = 'https://www.pushsafer.com/api'
    post_fields = {
        "t" : f'{name} send a message for Bytezo',
        "m" : message,
        "s" : 11,
        "v" : 3,
        "i" : 33,
        "c" : '#FF0000',
        "d" : 'a',
        "u" : 'https://www.pushsafer.com',
        "ut" : 'Open Pushsafer',
        "k" : key,
        }

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)