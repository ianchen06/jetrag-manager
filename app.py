from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    ctx = {'backcountry': '56000', 'greetings': 'hello,'}
    return render_template('index.html', **ctx)