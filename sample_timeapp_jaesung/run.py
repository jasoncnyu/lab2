from flask import Flask
from datetime import datetime  # Import the datetime module
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')  # Define a new route for "/time"
def current_time():
    now = datetime.now()  # Get the current date and time
    return now.strftime('%Y-%m-%d %H:%M:%S')  # Format it as a string

app.run(host='0.0.0.0',
        port=8080,
        debug=True)