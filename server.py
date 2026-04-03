# app.py

from flask import Flask

app = Flask(__name__)

# A simple "hello world" route
@app.route('/')
def home():
    return 'suresh was here'

# Start the server on port 3000
if __name__ == '__main__':
    app.run(port=3000)
