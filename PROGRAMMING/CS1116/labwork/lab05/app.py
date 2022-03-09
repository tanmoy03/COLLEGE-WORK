from flask import Flask, render_template, session
from flask_session import Session
from forms import GuessForm
from random import randint

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/guess", methods=["POST", "GET"])
def guess():
    form = GuessForm()
    guess = form.guess.data
    feedback = ""
    secret_no = randint(1,100)
    if form.validate_on_submit():
        if "sessionX" not in session:
            session["sessionX"] = secret_no
        else:
            if guess > session["sessionX"]:
                feedback = "Number is too high! Try something smaller :)"
            elif guess < session["sessionX"]:
                feedback = "Number is too low! Try a higher number :O"
            elif guess == session["sessionX"]:
                feedback = "You guessed right!!!"

        return render_template("guess.html", form=form, feedback=feedback, guess=session["sessionX"])
    return render_template("guess.html", form=form, feedback=feedback)    
    

            

            

        
        