from flask import Flask, render_template, request, flash

# to initialize the app, which takes in our main module represented by name, this command creates a class for our app
app = Flask(__name__)
app.secret_key = "jooniebearhoneymushroom" #password could be anything

# route for our app
@app.route("/")
def index():
  flash("What is your Name?")
  return render_template ("hello.html")

# this time we are interacting with server as well and collecting user input so using get method as well
@app.route('/greet', methods=["POST", "GET"])
def greet():
    flash("Hi! " + str(request.form['name_input']) + ", It is a pleasure to meet you!")
    return render_template("hello.html")

  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  # Start the Flask application
