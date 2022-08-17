from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

HELLO_HTML = """
    <html><body>
        <h1>Hello, {0}!</h1>
        The time is {1}.
    </body></html>"""

@app.route('/')
def index():
    return 'Hello world'

@app.route('/time')
def hello():
     name = request.args['name']
     return HELLO_HTML.format(name, str(datetime.now()))

@app.route('/mail')
def mail():
     name = request.args['name']
     mail = request.args['mail']
     return name+"  "+mail

@app.route('/data')
def name2():
    user = request.args.get('user')
    return user

