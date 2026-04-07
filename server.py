from flask import Flask #pip install flask
#this library is used to create a web server in python
app = Flask(__name__)

@app.route('/')
def home():
    return 'suresh was here'

# Start the server on port 3000
if __name__ == '__main__':
    app.run(port=3000)
