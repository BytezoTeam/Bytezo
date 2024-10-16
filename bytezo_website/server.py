from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for
)
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

    send_push(key=PUSH_SAVER_KEY, message=message, name=name)
    db.add_message(email=email, name=name, message=message)
    return redirect(url_for("index", send_message = True))
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

