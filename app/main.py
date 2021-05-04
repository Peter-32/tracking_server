from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        number = request.form['number']

        return 'Hello, World!'
