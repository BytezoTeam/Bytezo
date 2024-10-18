from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    jsonify
)
from http import HTTPStatus
from os import getenv
from bytezo_website.backend import send_push
from bytezo_website.database import database

DASHBOARD_PASS = getenv("ADMIN_PASS")
PUSH_SAVER_KEY = getenv("PUSH_SAVER_KEY")

db = database()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", send_message = request.args.get("send_message"))

@app.route("/send_message", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    message = db.add_message(email=email, name=name, message=message)
    send_push(key=PUSH_SAVER_KEY, id=message.id, name=message.name)
    return redirect(url_for("index", send_message = True))


@app.route("/get_message/<id>")
def get_message(id):
    if not id:
        return "", HTTPStatus.BAD_REQUEST
    
    message = db.get_message(id)
    return render_template("message.html", name=message.name, message=message.message, email=message.email)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

