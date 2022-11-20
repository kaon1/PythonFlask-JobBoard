from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')