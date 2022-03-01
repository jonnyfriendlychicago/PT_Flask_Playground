# the next two lines always need to be atop this server.py file 
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# all the @ stuff below will (later) be moved into separate files.  These will be replaced with controller import lines. 


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    # return 'Hello World (playground)'  # Return the string 'Hello World!' as a response
    return render_template("index.html", phrase="whatTheWhat", times=100)

# @app.route('/dojo')
# def dojo(): 
#     return "You're in the Dojo, baby!"

# # Create a route that responds with "Hi" and whatever name is in the URL after /say/
# @app.route('/say/<string:elNameo>')
# def hello(elNameo):
#     return f"Hiya, {elNameo}."

# # Create a route that responds with the given word repeated as many times as specified in the URL

# @app.route('/repeat/<int:multiplier>/<string:yourWord>')
# def greetaBunch(multiplier,yourWord ):
#     return f"{yourWord * multiplier}."


"""below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per cameron smith: 
@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'
# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

