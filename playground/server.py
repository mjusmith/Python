from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def render_box():
    colors = ['aqua']
    return render_template("playground.html", colors=colors) * 3

@app.route('/play/<int:number>')
def number(number):
    colors = ['aqua']
    return render_template("playground.html", colors=colors) * number

# @app.route('/play/<int:number>/<string:color>')
# def color(number, color):
#     return render_template("playground.html", bg_color=color) * number

if __name__=="__main__":
    app.run(debug=True)