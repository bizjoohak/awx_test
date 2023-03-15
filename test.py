from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>비즈데이터 좋아요!</h1><input type="textbox"/>'

app.run(host='0.0.0.0', port=8888)
