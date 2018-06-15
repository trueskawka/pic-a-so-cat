# Pairing ideas

## Fixing some bugs

1. Lines don't stop drawing when switching windows/moving outside of the canvas
    - maybe draw on click and hold?

2. Canvas offset is off when scrolling

<strike>3. After deleting the log file, the views need to be reloaded</strike>- yay!

## Adding new features

1. Add a second player - yay!
    
    Currently the drawing events are broadcasted and there is just one connection to the backend.

    To-do:

    <strike>- add another socket connection to separate the players</strike> 

    <strike>- create a random number for the id - just assign a random color</strike>

    <strike>- add info on the color to the log</strike>

    <strike>- adjust broadcast to include the color info</strike>
    
    <strike>- adjust the frontend to draw each segment with different color</strike>

2. Add new drawing tools 
    
    This is mostly building on the basic concept and using some basic canvas features. Maybe a good warmup?
    
    Some ideas: https://dev.opera.com/articles/html5-canvas-painting/

3. Add undo
    
    Since all the events are in the log, it might not be too painful to undo some strokes.

    Questions to consider:
    - what's a stroke? simplest case it would be just the last point in the log
    - if there is an undo, should there be a redo?

4. Download the log as an image

5. Add a menu for choosing colors

## Refactoring

1. Use Blueprints to split server logic
    
    I tried refactoring with Blueprints, but couldn't make the Flask-SocketIO to work with it. 
    I have all the code locally in the `flaskr` directory, so we could take a look at it.

2. Split out JS to separate files
    
    It would help with reusability of JS between different components.
    And maintenance, especially linting.

## Tooling

1. Set up sensible live-reloading
    
    Theoretically `python -m flask run` should work for live reloading, but it's not.
    We could explore it, though not sure how interesting it is - it's probably a solved problem.