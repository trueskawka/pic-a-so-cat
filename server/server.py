import os
import random
import gevent
from flask import Flask, render_template, send_from_directory, redirect, session
from flask_socketio import SocketIO, emit
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY']   = 'kitten'
app.config['NAMES_LOG']    = os.path.join(app.root_path, 'static/names_log')
app.config['CLICKS_LOG']   = os.path.join(app.root_path, 'static/clicks_log')
app.config['DRAWING_LOG']  = os.path.join(app.root_path, 'static/drawing_log')

Session(app)
socketio = SocketIO(app, manage_session=False)

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

# test socket connection
@socketio.on('connect')
def connected():
    print('connection established')

# create a log file
def create_log(log_file_path):
    log_file = open(log_file_path, 'w')
    log_file.close()

# append an event to a log
def append_log(log_file_path, data):
    try:
        log_file = open(log_file_path, 'a+')
    except IOError:
        create_log(log_file_path)
        log_file = open(log_file_path, 'a+')
    log_file.write(data + '\n')
    log_file.close()

# get current log state
def get_log(log_file_path):
    try:
        log_file = open(log_file_path, 'r')
    except IOError:
        create_log(log_file_path)
        log_file = open(log_file_path, 'r')
    log_data = log_file.read().split('\n')
    log_file.close()
    return log_data

# remove a log
def remove_log(log_file_path, path):
    if os.path.isfile(log_file_path):
        os.remove(log_file_path)
    else:    ## Show an error ##
        print("Error: %s file not found" % log_file_path)
    return redirect(path)

"""
Tracking clicks
"""
@app.route('/clicks')
def show_clicks():
    return render_template('clicks.html', log_data = get_log(app.config['CLICKS_LOG']))

@socketio.on('clck', namespace='/clicks')
def cnt(message):
    print('clicking')

@socketio.on('new click!', namespace='/clicks')
def add_click(data):
    append_log(app.config['CLICKS_LOG'], str(data[0]) + ':' + str(data[1]))
    emit('pixel clicked', { 'data' : data }, broadcast = True)

@socketio.on('clear clicks', namespace='/clicks')
def clear_clicks(msg):
    print('remove clicks log')
    remove_log(app.config['CLICKS_LOG'], '/clicks')

"""
Tracking mouse movements
"""
@app.route('/draw')
def show_drawing():
    return render_template('draw.html', log_data = get_log(app.config['DRAWING_LOG']))


# @app.route('/set/')
# def set():
#     session['key'] = 'value'
#     return 'ok'

@socketio.on('drw', namespace='/draw')
def drw_start(message):
    session['color'] = message
    print('drawing color: ', session['color'])

@socketio.on('draw', namespace='/draw')
def add_pixel(data):
    append_log(app.config['DRAWING_LOG'], 
               str(data[0]) + ':' + str(data[1]) + ':' + session['color'])
    emit('drawing', { 'data' : data, 'color': session['color'] }, broadcast = True)

@socketio.on('clear drawing', namespace='/draw')
def clear_drawing(msg):
    print('remove drawing log')
    remove_log(app.config['DRAWING_LOG'], '/draw')

"""
Generating names.
"""
# get a list of names from the file
def seed_names(file_path):
    text_file = open(file_path, 'r')
    words = text_file.read().split('\n')
    text_file.close()
    return words

words = seed_names('/usr/share/dict/propernames')

# generate a random name from the list
def generate_name(event_name, log_file_path):
    data = random.choice(words)
    append_log(log_file_path, data)
    print(data)
    emit(event_name, { 'data': data }, broadcast = True)

# on-click name generation route
@app.route('/names')
def show_words():   
    return render_template('names.html', log_data = get_log(app.config['NAMES_LOG']))

# the tutorial suggests namespace is optional, but it doesn't seem to be
@socketio.on('getname', namespace='/names')
def give_name(message):
    print('I\'ll get you a name!')
    generate_name('name', app.config['NAMES_LOG'])

# name stream route
@app.route('/generate')
def show_stream():
    return render_template('stream.html', log_data = get_log(app.config['NAMES_LOG']))

@socketio.on('generate stream', namespace='/generate')
def generate_words(message):
    print('I\'ll get you some names!')
    while True:
        generate_name('generated name', app.config['NAMES_LOG'])
        # to allow for updating on the frontend
        gevent.sleep(1)

if __name__ == '__main__':
    socketio.run(app)
