from flask import Flask, render_template, redirect, session  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def show_counter():
    if 'count' not in session:
        session['count']= 0
    return render_template('counter.html')

@app.route('/increment', methods=['POST'])
def increment():
    session['count']+= 1
    return redirect('/')



@app.route('/destroy')
def destruction():
    session.clear()
    return redirect('/')
    

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
