import os

from flask import Flask, request, abort
from markupsafe import escape
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_name():
    name = request.args.get("name")
    if name is None:
        return f"Hi Stranger"
    else:
        return f"Hi {escape(name)}"


@app.route('/user', methods=['GET', 'POST'])
def user():
    name = request.args.get("name")
    with open("./files/users.txt", "r+") as f:
        if request.method == "POST":
            for line in f:
                if name in line:
                    return f"{name} Already exists"
            f.write(name + "\n")
            return f"{name} added successfully!"
        if request.method == "GET":
            for line in f:
                if name in line:
                    return "You exist"
            abort(404)
        f.close()

