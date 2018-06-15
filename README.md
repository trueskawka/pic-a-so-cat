# PIC-a-so-CAT

PIC-a-so-CAT (_picaso-cat_ or _pick-a-socka_) is an in-browser drawing app. It allows you to connect 
to a server and start drawing, storing your creations in a friendly text format.

## Features

Current features: 

0. Server sending HTTP responses
- a simple Flask server returns HTML responses on `localhost:5000`

1. Server with a simple stream 
- the Flask server is streaming a list of proper names
- if you want to generate words on click, go to `localhost:5000/names`
- if you want to generate a stream of words, go to `localhost:5000/generate` (1 word per second)
- the stream is stored in a text file as a write-only log, you can download it at `localhost:5000/static/names_log`

2. Frontend sending clicks to the server
- your vanilla JavaScript frontend is sending clicks from a canvas element to the server
- the clicks are stored in a text file as a write-only log, you can download it at `localhost:5000/static/clicks_log`
- you can see all the clicks on `localhost:5000/clicks` - and add some more!

3. Connecting the dots
- your vanilla JavaScript frontend is drawing lines based on your mouse movement
- the lines are stored in a text file as a write-only log, you can download it at `localhost:5000/static/drawing_log`
- you can see the drawing on `localhost:5000/draw` - and add some more lines!

Planned features:

4. Drawing party
- anyone can connect to the server and start drawing, with a randomly assigned color
- all the drawings will be stored in the write-only log

5. Customizations
- instead of preassigned colors, you will be able to draw with any color you pick
- you will be able to download the drawing as an image
- if you manage to color every pixel on the canvas, the server will respond with a random cat picture

## Stack

Requirements: Python 3.6 backend, ES6/ES7 frontend, communication using websockets/REST API

## Installation

0. Set up a Python [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and run it

1. Install `requirements.txt` in your environment  

## Running

1. Set the Flask environment variable: `export FLASK_APP=server/server.py`

2. Run: `flask run` and go to `localhost:5000`

3. If you want live reloading, start the server with `python -m flask run` instead

## Reference

1. Flask-SocketIO docs - https://flask-socketio.readthedocs.io/en/latest/

2. Flask-SocketIO tutorial (a bit outdated) - https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent

3. On using `gevent.sleep()` - https://stackoverflow.com/questions/30901998/threading-true-with-flask-socketio

4. On using `DOMContentLoaded` - https://stackoverflow.com/questions/799981/document-ready-equivalent-without-jquery

## Copyright

1. Favicon [source](https://www.shareicon.net/cat-85580)

