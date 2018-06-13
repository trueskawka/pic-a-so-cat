import os
import random
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kitten'
socketio = SocketIO(app)

def seed_names(file_path):
    text_file = open(file_path, 'r')
    words = text_file.read().split('\n')
    text_file.close()
    return words

words = seed_names('/usr/share/dict/propernames')
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

def add_name(log_file_path):
    log_file = open(log_file_path, 'a+')
    name = random.choice(words)
    log_file.write(name + '\n')
    log_file.close()
    return name

def get_names(log_file_path):
    log_file = open(log_file_path, 'r')
    log_data = log_file.read().split('\n')
    log_file.close()
    return log_data

@app.route('/names')
def show_words():   
    return render_template('words.html', log_data = get_names(log_path))

@socketio.on('connect')
def connected():
    print('connection established')

@socketio.on('getname', namespace="/names")
def give_name(message):
    print('I\'ll get you a name')
    name = add_name(log_path)
    print(name)
    emit('name', { 'data': name })

if __name__ == '__main__':
    socketio.run(app)
