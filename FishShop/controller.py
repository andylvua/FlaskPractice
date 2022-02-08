from main import app


@app.route('/')
def index():
    return "Hooray"


@app.route('/fish/<_id>')
def get_fish(_id):
    print(_id)
    return "My fish is gorgeous"


@app.route("/fish", methods=["POST"])
def create_fish():
    print("Fish created")
    return "Fish created"
