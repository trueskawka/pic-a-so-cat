# PIC-a-so-CAT

PIC-a-so-CAT (_picaso-cat_ or _pick-a-socka_) is an in-browser drawing app. It allows you to connect 
to a server and start drawing, storing your creations in a friendly text format.

## Features

Current features: none

Planned features:

0. Server sending HTTP responses
- you will be able to connect to a simple Python 3.6 server
- it will send you a response in the form of an HTTP file

1. Server with a simple stream 
- your Python 3.6 server will be streaming a bunch of random words
- the words stream will be visible on `localhost:5000`
- the stream will be stored in a text file as a write-only log
- you will be able to download the log file

2. Frontend sending clicks to the server
- your vanilla JavaScript front-end will be sending clicks from a single user to the backend
- the clicks will be stored in a text file as a write-only log
- the clicks history will be visualized on `localhost:5000`

3. Connecting the dots
- your vanilla JavaScript frontend will be able to render lines based on mouse movement
- the lines will be stored in a text file as a write-only log
- the drawings will be visible on `localhost:5000`

4. Drawing party
- anyone can connect to the server and start drawing, with a randomly assigned color
- all the drawings will be stored in the write-only log

5. Customizations
- instead of preassigned colors, you will be able to draw with any color you pick
- you will be able to download the drawing as an image
- if you manage to color every pixel on the canvas, the server will respond with a random cat picture

## Stack

Requirements: Python 3.6 backend, ES6/ES7 frontend, communication using websockets/REST API