import os
import random
from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import Response

app = Flask(__name__)
text_file = open('/usr/share/dict/propernames', 'r')
words = text_file.read().split('\n')
text_file.close()
log_path = os.path.join(app.root_path, 'static/log')

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

@app.route('/names')
def feed_words():
    def add_name(log_file_path):
        log_file = open(log_file_path, 'a+')
        log_file.write(random.choice(words) + '\n')
        log_file.close()
    
    def get_names(log_file_path):
        log_file = open(log_file_path, 'r')
        log_data = log_file.read().split('\n')
        log_file.close()
        return log_data
    
    add_name(log_path)
    log_data = get_names(log_path)

    return render_template('words.html', log_data = log_data)