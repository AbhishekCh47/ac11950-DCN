from flask import Flask
from datetime import datetime
import pytz
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def curr_time():

    eastern = pytz.timezone('America/New_York')
    curr_time = datetime.now(eastern).strftime("%H:%M:%S %Z")
    return "Current time in New York: {}".format(curr_time)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
