# the next two lines always need to be atop this server.py file 
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# all the @ stuff below will (later) be moved into separate files.  These will be replaced with controller import lines. 


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def welcome():
    return render_template("index.html", displayThisMany = 0, displayThisColorYknow = "aqua") 

@app.route('/play')
def play():
    return render_template("index.html", displayThisMany=70, displayThisColorYknow = "aqua")

@app.route('/play/<int:num>')
def playNumber(num):
    return render_template("index.html", displayThisMany=num, displayThisColorYknow = "aqua")

@app.route('/play/<int:num>/<string:incomingColor>')
def playNumberColor(num, incomingColor):
    if incomingColor == "blue": 
        selectedColor = "blue" 
    elif incomingColor == "green": 
        selectedColor = "green"
    else: 
        selectedColor = "red"
    # selectedColor = incomingColor 
    return render_template("index.html", displayThisMany=num, displayThisColorYknow = selectedColor )


"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per cameron smith: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

