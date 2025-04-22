from http import HTTPStatus
from os import getenv

from flask import Flask, redirect, render_template, request, url_for, make_response
from flask import Response as FlaskResponse
from werkzeug.wrappers.response import Response as WerkzeugResponse
from dotenv import load_dotenv

from bytezo_website.backend import send_push
from bytezo_website.database import Database, add_message, get_message


load_dotenv()
DASHBOARD_PASS = getenv("ADMIN_PASS")
PUSH_SAVER_KEY = getenv("PUSH_SAVER_KEY")
if not PUSH_SAVER_KEY:
    print("PUSH_SAVER_KEY not set")
if not DASHBOARD_PASS:
    print("DASHBOARD_PASS is not set")
BYTEZO_ANALYTICS_URL = getenv("BYTEZO_ANALYTICS_URL")
if not BYTEZO_ANALYTICS_URL:
    print("BYTEZO_ANALYTICS_URL is not set")

db = Database()
app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html", send_message=request.args.get("send_message"), BYTEZO_ANALYTICS_URL=BYTEZO_ANALYTICS_URL)


@app.route("/send_message", methods=["POST"])
def send_message_route() -> FlaskResponse | WerkzeugResponse:
    if not PUSH_SAVER_KEY:
        return make_response("", HTTPStatus.GONE)

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    if not name or not email or not message:
        return make_response("", HTTPStatus.BAD_REQUEST)

    message = add_message(email=email, name=name, message=message)
    send_push(key=PUSH_SAVER_KEY, message_id=str(message.id), name=str(message.name))
    return redirect(url_for("index", send_message=True))


@app.route("/get_message/<id>")
def get_message_route(message_id: str) -> FlaskResponse | str:
    if not message_id:
        return make_response("", HTTPStatus.BAD_REQUEST)

    message = get_message(message_id)
    return render_template("message.html", name=message.name, message=message.message, email=message.email)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
