from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/play')
def render_box():
    return render_template("playground.html") *3

@app.route('/play/<int:number>')
def number(number):
    return render_template("playground.html") * number

@app.route('/play/<int:number>/<string:color>')
def color(number, color):
    return render_template("playground.html", bg_color=color) * number

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.