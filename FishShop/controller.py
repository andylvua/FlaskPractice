from main import app, db
from models import Fish
from flask import request


@app.route('/')
def index():
    return "Hooray"


@app.route('/fish/<_id>')
def get_fish(_id):
    print(_id)
    return "My fish is gorgeous"


@app.route("/fish", methods=["POST"])
def create_fish():
    print(request.json["name"])
    print(request.json["origin"])

    fish = Fish(name=request.json["name"], origin=request.json["origin"])
    db.session.add(fish)

    db.session.commit()

    print(Fish.query.all())
    return "Fish created"
