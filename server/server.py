import os
from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def hellooo():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(not_found):
    return render_template('404.html'), 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
