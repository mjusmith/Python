from flask import Flask, render_template, session, redirect, request  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "I actually am a zombie"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def look_at_the_form():
    return render_template('survey.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comments']=request.form['comments']
    # session['zombie_check']=request.form['zombie_check']
    session['zombie_integrity']=request.form['zombie_integrity']
    # if request.method == 'POST':
    #     if 'zombie_integrity' in request.form:
    #         checkbox_value = request.form['zombie_integrity']
    #         checkbox_value == 'on'
    #         return "I still think you're lying"
    #     else:
    #         return 'Scared to get caught?'
    return redirect ('/result')

@app.route('/result')
def view_zults():
    return render_template('result.html')

@app.route('/cleanup')
def clear():
    session.clear()
    return redirect ('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.