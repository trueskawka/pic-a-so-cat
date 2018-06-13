import os
import random
import gevent
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kitten'
socketio = SocketIO(app)

# get a list of names from the file
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

# append to file
def add_name(log_file_path):
    log_file = open(log_file_path, 'a+')
    name = random.choice(words)
    log_file.write(name + '\n')
    log_file.close()
    return name

# get current log state
def get_names(log_file_path):
    log_file = open(log_file_path, 'r')
    log_data = log_file.read().split('\n')
    log_file.close()
    return log_data

# generate a random name from the list
def generate_name(event_name, log_file_path):
    name = add_name(log_file_path)
    print(name)
    emit(event_name, { 'data': name })

# test socket connection
@socketio.on('connect')
def connected():
    print('connection established')

# on-click name generation route
@app.route('/names')
def show_words():   
    return render_template('words.html', log_data = get_names(log_path))

# the tutorial suggests namespace is optional, but it doesn't seem to be
@socketio.on('getname', namespace='/names')
def give_name(message):
    print('I\'ll get you a name!')
    generate_name('name', log_path)

# name stream route
@app.route('/generate')
def show_stream():
    return render_template('stream.html', log_data = get_names(log_path))

@socketio.on('generate stream', namespace='/generate')
def generate_words(message):
    print('I\'ll get you some names!')
    while True:
        generate_name('generated name', log_path)
        # to allow for updating on the frontend
        gevent.sleep(1)

if __name__ == '__main__':
    socketio.run(app)
