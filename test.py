from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '안녕하세요'

app.run(host='0.0.0.0', port=8888)
